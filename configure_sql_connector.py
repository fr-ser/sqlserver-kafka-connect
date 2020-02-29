"""Configures a Kafka Connector for Postgres Station data"""

import json

import requests

from config import (
    KAFKA_CONNECT_URL,
    JDBC_CONNECTION_URL, JDBC_CONNECTION_USER, JDBC_CONNECTION_PASSWORD,
)


def add_increasing_connector():
    connector_name = "SQL_INCREASING_ID_CONNECTOR"
    table_name = "kafka.dbo.increasing_ids"

    resp = requests.post(
        f"{KAFKA_CONNECT_URL}/connectors",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "name": connector_name,
            "config": {
                "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
                "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                "key.converter.schemas.enable": "false",
                "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                "value.converter.schemas.enable": "false",
                "batch.max.rows": "500",
                "connection.url": JDBC_CONNECTION_URL,
                "connection.user": JDBC_CONNECTION_USER,
                "connection.password": JDBC_CONNECTION_PASSWORD,
                "table.whitelist": table_name,
                "topic.prefix": "connect.",
                "poll.interval.ms": "1000",
                # key generation
                "transforms": "createKey,extractInt",
                "transforms.createKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
                "transforms.createKey.fields": "id_num",
                "transforms.extractInt.type": "org.apache.kafka.connect.transforms.ExtractField$Key",
                "transforms.extractInt.field": "id_num",
                # mode specific settings
                "mode": "incrementing",
                "incrementing.column.name": "id_num",
            }
        }),
        timeout=10,
    )

    resp.raise_for_status()
    print(f"Kafka Connect {connector_name} created successfully")


def add_updated_at_connector():
    connector_name = "SQL_UPDATED_AT_CONNECTOR"
    table_name = "kafka.dbo.updated_at"

    resp = requests.post(
        f"{KAFKA_CONNECT_URL}/connectors",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "name": connector_name,
            "config": {
                "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
                "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                "key.converter.schemas.enable": "false",
                "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                "value.converter.schemas.enable": "false",
                "batch.max.rows": "500",
                "connection.url": JDBC_CONNECTION_URL,
                "connection.user": JDBC_CONNECTION_USER,
                "connection.password": JDBC_CONNECTION_PASSWORD,
                "table.whitelist": table_name,
                "topic.prefix": "connect.",
                "poll.interval.ms": "1000",
                # key generation
                "transforms": "createKey,extractInt",
                "transforms.createKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
                "transforms.createKey.fields": "id_num",
                "transforms.extractInt.type": "org.apache.kafka.connect.transforms.ExtractField$Key",
                "transforms.extractInt.field": "id_num",
                # mode specific settings
                "mode": "timestamp",
                "timestamp.column.name": "updated_at",
            }
        }),
        timeout=10,
    )

    resp.raise_for_status()
    print(f"Kafka Connect {connector_name} created successfully")


def add_no_hints_connector():
    connector_name = "SQL_NO_HINTS_CONNECTOR"
    table_name = "kafka.dbo.no_hints"

    resp = requests.post(
        f"{KAFKA_CONNECT_URL}/connectors",
        headers={"Content-Type": "application/json"},
        data=json.dumps({
            "name": connector_name,
            "config": {
                "connector.class": "io.confluent.connect.jdbc.JdbcSourceConnector",
                "key.converter": "org.apache.kafka.connect.json.JsonConverter",
                "key.converter.schemas.enable": "false",
                "value.converter": "org.apache.kafka.connect.json.JsonConverter",
                "value.converter.schemas.enable": "false",
                "batch.max.rows": "500",
                "connection.url": JDBC_CONNECTION_URL,
                "connection.user": JDBC_CONNECTION_USER,
                "connection.password": JDBC_CONNECTION_PASSWORD,
                "table.whitelist": table_name,
                "topic.prefix": "connect.",
                "poll.interval.ms": "1000",
                # key generation
                "transforms": "createKey,extractInt",
                "transforms.createKey.type": "org.apache.kafka.connect.transforms.ValueToKey",
                "transforms.createKey.fields": "id_num",
                "transforms.extractInt.type": "org.apache.kafka.connect.transforms.ExtractField$Key",
                "transforms.extractInt.field": "id_num",
                # mode specific settings
                "mode": "bulk",
            }
        }),
        timeout=10,
    )

    resp.raise_for_status()
    print(f"Kafka Connect {connector_name} created successfully")


if __name__ == "__main__":
    add_increasing_connector()
    add_updated_at_connector()
    add_no_hints_connector()
