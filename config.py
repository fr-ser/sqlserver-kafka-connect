import os

KAFKA_SERVER = os.environ.get("KAFKA_SERVER", "kafka:29092")

KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")

JDBC_CONNECTION_URL = os.environ.get("JDBC_CONNECTION_URL", "jdbc:jtds:sqlserver://mssql:1433")
JDBC_HOSTNAME, JDBC_PORT = JDBC_CONNECTION_URL.split("//")[1].split(":")

JDBC_CONNECTION_DATABSE = os.environ.get("JDBC_CONNECTION_DATABSE", "kafka")

JDBC_CONNECTION_USER = os.environ.get("JDBC_CONNECTION_USER", "SA")
JDBC_CONNECTION_PASSWORD = os.environ.get("JDBC_CONNECTION_PASSWORD", "Passw0rdOfs3cr3ts")
