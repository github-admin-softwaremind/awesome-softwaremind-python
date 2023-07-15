import logging

logger = logging.getLogger(__name__)
logger.propagate = False


class CustomFormatter(logging.Formatter):
    # Formatters use emit method when logging the message
    def format(self, record):
        s = super().format(record)
        return f"###### {s} ######"


handler1, handler2 = logging.StreamHandler(), logging.StreamHandler()
fmt1 = CustomFormatter()
# We set a formatter for every handler
handler1.setFormatter(fmt1)
logger.addHandler(handler1)
# In most cases you can just set the format. Many useful fields are evaluated
fmt2 = logging.Formatter("%(asctime)s|%(levelname)s|%(message)s|")
handler2.setFormatter(fmt2)
logger.addHandler(handler2)

# This will log two things because every handler will call emit
# handler1 log: ###### ABC ######
# handler2 log: 2023-07-15 19:27:36,675|WARNING|ABC|
logger.warning("ABC")
