## Schema changes

see https://debezium.io/documentation/reference/1.0/connectors/sqlserver.html#schema-evolution

Events including the new event can be caputured, but no event just for the schema change is emitted.

Example:

```sql
INSERT INTO kafka.dbo.ship VALUES ('old', '1');
ALTER TABLE kafka.dbo.ship ADD new_ int;
INSERT INTO kafka.dbo.ship VALUES ('new', '2', 2);

EXEC sys.sp_cdc_enable_table @source_schema = 'dbo', @source_name = 'ship', @role_name = NULL,
    @supports_net_changes = 0, @capture_instance = 'v2-ship';
INSERT INTO kafka.dbo.ship VALUES ('new', '3', 3);
```
