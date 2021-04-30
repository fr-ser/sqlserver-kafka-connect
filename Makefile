install:
	pipenv install --python 3.7.9 --dev

bootstrap-slim:
	docker-compose --file docker-compose.slim.yaml down --remove-orphans --volumes --timeout=5 > /dev/null
	docker-compose --file docker-compose.slim.yaml build > /dev/null

	docker-compose --file docker-compose.slim.yaml up --detach sqlserver postgres > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm kafka-cli > /dev/null
	docker-compose --file docker-compose.slim.yaml up --detach kafka-connect > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm wait-for-db > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm sqlserver-cli

	make --no-print-directory connectors-install

bootstrap:
	docker-compose down --remove-orphans --volumes --timeout=5 > /dev/null
	docker-compose build > /dev/null

	docker-compose up --detach sqlserver postgres > /dev/null
	docker-compose run --rm kafka-cli > /dev/null
	docker-compose up --detach kafka-connect > /dev/null
	docker-compose run --rm wait-for-db > /dev/null
	docker-compose run --rm sqlserver-cli

	make --no-print-directory connectors-install

connectors-install:
	./wait_for_kafka_connect.sh
	curl --silent -X POST -H "Content-Type: application/json" -d @connector-configs/debezium.json http://localhost:8083/connectors/ | jq .
	curl --silent -X POST -H "Content-Type: application/json" -d @connector-configs/postgres.json http://localhost:8083/connectors/ | jq .


connectors-delete:
	curl --silent -X DELETE http://localhost:8083/connectors/debezium-source/ | jq .
	curl --silent -X DELETE http://localhost:8083/connectors/jdbc-sink/ | jq .

test-no-bootstrap:
	PYTHONPATH=./src pipenv run pytest tests

test: bootstrap test-no-bootstrap

insert-1:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/1_initial_insert.sql

insert-2:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/2_update_data.sql

insert-3:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/3_delete_data.sql
