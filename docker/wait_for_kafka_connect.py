import os
import time

import requests

KAFKA_CONNECT_URL = os.environ.get("KAFKA_CONNECT_URL", "http://localhost:8083")


def check_kafka_connect(timeout=45):
    end_time = time.time() + timeout

    print(f"Waiting for kafka-connect")
    while time.time() < end_time:
        try:
            resp = requests.get(f"{KAFKA_CONNECT_URL}/connector-plugins")
            resp.raise_for_status()
            # list of plugins should not be empty
            return
        except Exception:
            time.sleep(0.3)
            continue
    else:
        raise Exception(f"Could find plugins for kafka-connect")


if __name__ == "__main__":
    check_kafka_connect()
