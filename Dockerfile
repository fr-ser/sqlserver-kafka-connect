FROM confluentinc/cp-kafka-connect-base:6.0.0

RUN confluent-hub install --no-prompt debezium/debezium-connector-sqlserver:1.5.0
RUN confluent-hub install --no-prompt confluentinc/kafka-connect-jdbc:10.0.0

ENV CONNECT_PLUGIN_PATH="/usr/share/confluent-hub-components,/usr/share/java/kafka"