install:
	pipenv install --python 3.7.9 --dev


bootstrap-slim:
	docker-compose --file docker-compose.slim.yaml  down --remove-orphans --volumes --timeout=5
	docker-compose --file docker-compose.slim.yaml build
	docker-compose --file docker-compose.slim.yaml up -d sqlserver postgres
	docker-compose --file docker-compose.slim.yaml run kafka-cli
	docker-compose --file docker-compose.slim.yaml up -d kafka-connect
	docker-compose --file docker-compose.slim.yaml run sqlserver-cli
	docker-compose --file docker-compose.slim.yaml up -d faust
	docker-compose --file docker-compose.slim.yaml run debezium

bootstrap:
	docker-compose down --remove-orphans --volumes --timeout=5
	docker-compose build
	docker-compose up -d sqlserver postgres
	docker-compose run kafka-cli
	docker-compose up -d kafka-connect
	docker-compose run sqlserver-cli
	docker-compose up -d faust
	docker-compose run debezium

test-no-bootstrap:
	PYTHONPATH=./src pipenv run pytest tests

test: bootstrap test-no-bootstrap

insert-1:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/1_initial_insert.sql

insert-2:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/2_update_data.sql

insert-3:
	docker-compose run sqlserver-cli /opt/mssql-tools/bin/sqlcmd -S sqlserver -U SA -P Passw0rdOfs3cr3ts -i /data/3_delete_data.sql
