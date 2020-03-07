import time

import psycopg2
from psycopg2.extras import RealDictCursor
import pyodbc
import pytest

from config import DB_NAME, DB_HOST, DB_PASSWORD, DB_USER, POSTGRES_URI


@pytest.fixture
def sql_server_cursor():
    cnxn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server}"
        f";SERVER={DB_HOST}"
        f";DATABASE={DB_NAME}"
        f";UID={DB_USER}"
        f";PWD={DB_PASSWORD}",
        autocommit=True,
        timeout=10,
    )
    cur = cnxn.cursor()
    cur.execute(f"DELETE FROM {DB_NAME}.dbo.ship")
    cur.execute(f"DELETE FROM {DB_NAME}.dbo.train")
    yield cur
    cnxn.close()


def get_postgres_ship_rows(result_check=None, timeout=10, row_count=None):
    """
    :param result_check: function to check if result is ok.
                         This function must return a boolean
    :param row_count: if no result_check, but a row_count is passed
                      A result_check for the exact row_count is used
    :param timeout: timeout how long to repeat the query
                    until the result check is satisfied
    """

    if not result_check and row_count is None:
        raise ValueError("Need result_check or row_count")
    elif not result_check:
        def result_check(rows):
            return len(rows) == row_count

    end_time = time.time() + timeout

    with psycopg2.connect(dsn=POSTGRES_URI, connect_timeout=5) as con:
        with con.cursor(cursor_factory=RealDictCursor) as cur:
            while time.time() < end_time:
                cur.execute(f"SELECT * FROM public.ship ORDER BY vessel_id;")
                result = cur.fetchall()

                if result_check(result):
                    return result
                else:
                    time.sleep(0.3)

    raise Exception(
        f"Timed out getting the table without getting valid result. Invalid Result: {result}"
    )
