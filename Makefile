install:
	pipenv install --python 3.7.9 --dev

bootstrap-slim:
	docker-compose --file docker-compose.slim.yaml down --remove-orphans --volumes --timeout=5 > /dev/null
	docker-compose --file docker-compose.slim.yaml build > /dev/null

	docker-compose --file docker-compose.slim.yaml up -d sqlserver postgres > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm kafka-cli > /dev/null
	docker-compose --file docker-compose.slim.yaml up -d kafka-connect faust > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm wait-for-db > /dev/null
	docker-compose --file docker-compose.slim.yaml run --rm sqlserver-cli

	SLEEP_LENGTH=5 ./deploy_connector.sh

bootstrap:
	docker-compose down --remove-orphans --volumes --timeout=5 > /dev/null
	docker-compose build > /dev/null

	docker-compose up -d sqlserver postgres > /dev/null
	docker-compose run --rm kafka-cli > /dev/null
	docker-compose up -d kafka-connect faust > /dev/null
	docker-compose run --rm wait-for-db > /dev/null
	docker-compose run --rm sqlserver-cli

	SLEEP_LENGTH=5 ./deploy_connector.sh

connector-install:
	./deploy_connector.sh

connector-delete:
	curl --silent -X DELETE http://localhost:8083/connectors/DEBEZIUM_CONNECTOR/ | jq .

test-no-bootstrap:
	PYTHONPATH=./src pipenv run pytest tests

test: bootstrap test-no-bootstrap

insert-1:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/1_initial_insert.sql

insert-2:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/2_update_data.sql

insert-3:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/3_delete_data.sql
