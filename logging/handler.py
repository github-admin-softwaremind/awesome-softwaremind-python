import logging

logger = logging.getLogger(__name__)
logger.propagate = False


class MultiplyHandler(logging.StreamHandler):
    # Handlers use emit method when logging the message
    def emit(self, record):
        msg = record.getMessage()
        if msg.isdigit():
            # If message is a digit, let's modify it
            record.msg = int(msg) * 2
        super().emit(record)


logger.addHandler(MultiplyHandler())
logger.warning("ABC")  # logs ABC
logger.warning("111")  # logs 222
