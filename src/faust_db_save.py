import asyncpg
import faust
from loguru import logger

from config import FAUST_BROKER_LIST, TOPIC_SHIP, POSTGRES_URI
from faust_helper import Operations, setup_crash_handler, crash_app


app = faust.App(
    "db-save",
    broker=FAUST_BROKER_LIST,
    store="memory://",
    options={
        "topic_disable_leader": True,
    },
)

source_topics = app.topic(TOPIC_SHIP)


async def db_save(db_connection, payload):
    table = f"public.{payload['source']['table']}"
    if payload["op"] in (Operations.insert, Operations.snapshot):
        columns_str = ", ".join(payload["after"].keys())
        values = list(payload["after"].values())
        placeholders = ", ".join(f"${idx}" for idx in range(1, len(values)+1))

        await db_connection.execute(
            f"""
            INSERT INTO {table} ({columns_str}) VALUES ({placeholders})
            -- conflict handling due to possible duplicates during snapshot generation
            ON CONFLICT DO NOTHING;
            """,
            *values
        )
    elif payload["op"] == Operations.update:
        update_columns = ", ".join(
            f"{column} = ${idx}"
            for idx, column in enumerate(payload["after"].keys(), start=1)
        )
        values = list(payload["after"].values())

        await db_connection.execute(
            f"""
                UPDATE {table} SET {update_columns}
                WHERE vessel_id = {payload['after']['vessel_id']}
            """,
            *values
        )
    elif payload["op"] == Operations.delete:
        await db_connection.execute(
            f"DELETE FROM {table} WHERE vessel_id = {payload['before']['vessel_id']}"
        )


async def save_could_crash(stream):
    try:
        connection = await asyncpg.connect(POSTGRES_URI, timeout=5)
        logger.debug("Connected to database")
    except Exception:
        logger.warning("Could not connect to the database")
        raise

    async for item in stream:
        if item is None:
            pass
            # Tombstone, delete comes separate
        elif item["op"] in Operations.all_:
            await db_save(connection, item)
        else:
            raise NotImplementedError(f"Operation unknown: {item}")


@app.agent(source_topics)
async def save_agent(stream):
    try:
        await save_could_crash(stream)
    except Exception:
        logger.exception("Critical Exception. Exiting")
        await crash_app(app)


setup_crash_handler()

if __name__ == "__main__":
    app.main()
