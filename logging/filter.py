import logging

logger = logging.getLogger(__name__)
logger.propagate = False


class StartWithA(logging.Filter):
    # For every emited message we call a filter. If it returns False, the log is dropped
    def filter(self, record):
        return record.getMessage().startswith("A")


class EndsWithB(logging.Filter):
    def filter(self, record):
        return record.getMessage().endswith("B")


class NoParsingFilter(logging.Filter):
    # For every emited message we call a filter. If it returns False, the log is dropped
    def filter(self, record):
        return not record.getMessage().startswith("A")


handler = logging.StreamHandler()
# We can add filters to both, handlers and loggers
handler.addFilter(EndsWithB())
logger.addHandler(handler)
logger.addFilter(StartWithA())

logger.warning("ABC")  # Filtered by the logger
logger.warning("CBA")  # Filtered by the handler
logger.warning("ACB")  # Finally! Logs ACB
