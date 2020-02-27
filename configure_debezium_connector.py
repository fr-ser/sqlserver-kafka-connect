"""Configures a Kafka Connector for Postgres Station data"""

import json

import requests

from config import (
    KAFKA_CONNECT_URL, KAFKA_SERVER,
    JDBC_CONNECTION_USER, JDBC_CONNECTION_PASSWORD, JDBC_CONNECTION_DATABSE,
    JDBC_HOSTNAME, JDBC_PORT,
)


def add_connector():
    connector_name = "DEBEZIUME_INCREASING_ID_CONNECTOR"
    # table_name = "kafka.dbo.increasing_ids"

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
                "database.history.kafka.topic": "__debezium.dbhistory"
            }
        }),
        timeout=10,
    )

    resp.raise_for_status()
    print(f"Kafka Connect {connector_name} created successfully")


if __name__ == "__main__":
    add_connector()
