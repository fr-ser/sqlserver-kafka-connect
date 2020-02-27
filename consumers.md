```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --property print.key=true --topic connect.kafka_increasing_ids --from-beginning
```

```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --property print.key=true --topic connect.kafka_updated_at --from-beginning
```

```
./kafka-console-consumer.sh --bootstrap-server localhost:9092 --property print.key=true --topic connect.kafka_no_hints --from-beginning
```
