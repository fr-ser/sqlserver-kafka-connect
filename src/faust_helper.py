import os
import signal

from loguru import logger


class Operations:
    delete = "d"
    insert = "c"
    snapshot = "r"
    update = "u"
    all_ = ["d", "c", "r", "u"]


def alarm_handler(signum, frame):
    logger.info(f'Alarm signal handler called with signal {signum}')
    # os._exit is a very severe exit.
    # It does not close handlers or flush buffers.
    # But here it is our only choice, to also crash docker containers
    os._exit(1)


async def crash_app(app):
    # raise an alarm and stop anyways
    # if after 30 seconds the app is still running
    signal.alarm(30)

    logger.info("Initiating stopping application")
    await app.stop()
    logger.debug("Stopping finished")
    # os._exit is a very severe exit.
    # It does not close handlers or flush buffers.
    # But here it is our only choice, to also crash docker containers
    os._exit(1)


def setup_crash_handler():
    signal.signal(signal.SIGALRM, alarm_handler)
