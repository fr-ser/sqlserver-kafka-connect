import os


KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "kafka:29092")
KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_DEBEZIUM_HOST = os.environ.get("DB_HOST", "mssql")
DB_PORT = os.environ.get("DB_PORT", "1433")
DB_NAME = os.environ.get("DB_NAME", "kafka")
DB_USER = os.environ.get("DB_USER", "SA")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "Passw0rdOfs3cr3ts")
