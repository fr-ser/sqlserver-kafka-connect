from collections import namedtuple

from .conftest import get_postgres_ship_rows

from config import DB_NAME

ShipPort = namedtuple("ShipPort", "ship port")


def test_insert(sql_server_cursor):
    values = [
        ShipPort("a", "port of a"),
        ShipPort("b", "port of b"),
        ShipPort("c", "port of c"),
    ]

    sql_server_cursor.executemany(
        f"INSERT INTO {DB_NAME}.dbo.ship (ship, port) VALUES(?, ?);",
        values,
    )

    pg_rows = get_postgres_ship_rows(row_count=len(values))

    for pg_row, value in zip(pg_rows, values):
        assert pg_row["ship"] == value[0]
        assert pg_row["port"] == value[1]


def test_update(sql_server_cursor):
    old_value = ShipPort("a", "port of a")
    new_value = ShipPort("new a", "new port of a")

    sql_server_cursor.execute(
        f"INSERT INTO {DB_NAME}.dbo.ship (ship, port) VALUES(?, ?);",
        old_value,
    )

    sql_server_cursor.execute(
        f"UPDATE {DB_NAME}.dbo.ship SET ship = ?, port = ? where ship =?",
        (new_value.ship, new_value.port, old_value.ship),
    )

    def check_function(rows):
        return (
            len(rows) == 1 and
            rows[0]["ship"] == new_value.ship and
            rows[0]["port"] == new_value.port
        )

    assert get_postgres_ship_rows(result_check=check_function)


def test_delete(sql_server_cursor):
    # delete is also implicitly tested by the cleanup between tests
    value = ShipPort("a", "port of a")

    sql_server_cursor.execute(
        f"INSERT INTO {DB_NAME}.dbo.ship (ship, port) VALUES(?, ?);",
        value,
    )
    assert get_postgres_ship_rows(row_count=1)

    sql_server_cursor.execute(f"DELETE FROM {DB_NAME}.dbo.ship")

    assert not get_postgres_ship_rows(row_count=0)
