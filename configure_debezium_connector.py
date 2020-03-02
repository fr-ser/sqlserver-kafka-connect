"""Configures a Kafka Connector for Postgres Station data"""

import json
import os

import requests


KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "kafka:29092")
KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")
JDBC_HOSTNAME = os.environ.get("JDBC_HOSTNAME", "mssql")
JDBC_PORT = os.environ.get("JDBC_PORT", "1433")
JDBC_CONNECTION_DATABSE = os.environ.get("JDBC_CONNECTION_DATABSE", "kafka")
JDBC_CONNECTION_USER = os.environ.get("JDBC_CONNECTION_USER", "SA")
JDBC_CONNECTION_PASSWORD = os.environ.get("JDBC_CONNECTION_PASSWORD", "Passw0rdOfs3cr3ts")


def add_connector():
    connector_name = "DEBEZIUM_CONNECTOR"
    table_whitelist = r".*increasing_ids,.*updated_at,.*no_hints"

    resp = requests.post(
        f"{KAFKA_CONNECT_URL}/connectors",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "name": connector_name,
            "config": {
                "connector.class": "io.debezium.connector.sqlserver.SqlServerConnector",
                "tasks.max": "1",
                "database.server.name": "main",
                "database.hostname": JDBC_HOSTNAME,
                "database.port": JDBC_PORT,
                "database.user": JDBC_CONNECTION_USER,
                "database.password": JDBC_CONNECTION_PASSWORD,
                "database.dbname": JDBC_CONNECTION_DATABSE,
                "database.history.kafka.bootstrap.servers": KAFKA_SERVER,
                "database.history.kafka.topic": "__debezium.dbhistory",
                "table.whitelist": table_whitelist,
            }
        }),
        timeout=10,
    )

    resp.raise_for_status()
    print(f"Kafka Connect {connector_name} created successfully")


if __name__ == "__main__":
    add_connector()
