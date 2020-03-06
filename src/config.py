import os
import re


KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "localhost:9092")
DB_HOST = os.environ.get("DB_HOST", "localhost")
KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")
DEBEZIUM_DB_HOST = os.environ.get("DEBEZIUM_DB_HOST", "mssql")
DEBEZIUM_KAFKA_SERVER = os.environ.get("DEBEZIUM_KAFKA_SERVER", "kafka:29092")
DB_PORT = os.environ.get("DB_PORT", "1433")
DB_NAME = os.environ.get("DB_NAME", "kafka")
DB_USER = os.environ.get("DB_USER", "SA")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Passw0rdOfs3cr3ts")

POSTGRES_URI = os.environ.get(
    "POSTGRES_URI", "postgresql://SA:Passw0rdOfs3cr3ts@localhost:5432/kafka",
)


_cleaned_broker_list = re.sub(r"[A-Za-z]+://", "", KAFKA_SERVER)
FAUST_BROKER_LIST = [f"kafka://{broker}" for broker in _cleaned_broker_list.split(",")]

TOPIC_SHIP = os.environ.get("TOPIC_SHIP", "main.dbo.ship")
TOPICS_TRAIN = os.environ.get("TOPICS_TRAIN", "main.dbo.train")
