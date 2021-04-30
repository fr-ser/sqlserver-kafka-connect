# SQL Server / MS SQL - Kafka Connect - Debezium - PoC

This is a small demo application to load data from a MS SQL / SQL Server database (via the
Debezium source connector) into Kafka and then forward the data into a Postgres database (via the
JDBC sink connector).

## Requirements

- docker and docker-compose
- bash (probably whole linux environment)

## Startup

To start the full (3 kafka brokers 2 kafka connect) environment: `make bootstrap`

To start a slim (1 kafka broker 1 kafka connect) environment: `make bootstrap-slim`

## Demo

You can run the following commands and see the effects in the source and target database

```bash
make insert-1 # insert records
make insert-2 # insert and update
make insert-3 # delete
```

## Credentials

For both databases the user is `SA` and the password is `Passw0rdOfs3cr3ts`.

## Schema changes

see <https://debezium.io/documentation/reference/1.0/connectors/sqlserver.html#schema-evolution>

Events including the new event can be captured, but no event just for the schema change is emitted.

Example:

```sql
INSERT INTO kafka.dbo.ship VALUES ('old', '1');
ALTER TABLE kafka.dbo.ship ADD new_ int;
INSERT INTO kafka.dbo.ship VALUES ('new', '2', 2);

EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'ship', @role_name = NULL,
    @supports_net_changes = 0, @capture_instance = 'v2-ship';
INSERT INTO kafka.dbo.ship VALUES ('new', '3', 3);
```
