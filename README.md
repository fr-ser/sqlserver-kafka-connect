# SQL Server / MS SQL - Kafka Connect - Debezium - PoC

## Requirements

- python3
- pipenv
- docker and docker-compose
- bash (probably whole linux environment)

## Startup

To start the full (3 kafka brokers 2 kafka connect) environment: `make bootstrap`

To start a slim (1 kafka broker 1 kafka connect) environment: `make bootstrap-slim`

## Tests

To run the tests: `make test-no-bootstrap`

To run the tests and starting the environment: `make test`

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
