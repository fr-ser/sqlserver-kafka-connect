import os

KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")
JDBC_CONNECTION_URL = os.environ.get("JDBC_CONNECTION_URL", "jdbc:jtds:sqlserver://mssql:1433")
JDBC_CONNECTION_USER = os.environ.get("JDBC_CONNECTION_USER", "SA")
JDBC_CONNECTION_PASSWORD = os.environ.get("JDBC_CONNECTION_PASSWORD", "Passw0rdOfs3cr3ts")
