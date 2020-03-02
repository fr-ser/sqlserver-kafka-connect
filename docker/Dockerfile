FROM python:3.7-alpine

WORKDIR /usr/src/app
RUN pip install --no-cache-dir pipenv

COPY Pipfile Pipfile.lock ./
RUN pipenv install --system

COPY configure_debezium_connector.py .
COPY ./docker/wait_for_kafka_connect.py .

CMD python ./wait_for_kafka_connect.py && python ./configure_debezium_connector.py
