import logging

# Should be always called unless you know what are you doing
# We create logger based on filename instead of using root one (from logging calls)
logger = logging.getLogger(__name__)
# Sets a basic configuration - StreamHandler, with Formatter
logging.basicConfig()
# Prints nothing - default level is WARNING (30)
logger.info("A")
# In real our new logger instance has no handlers, it is handled with root default handler created during basicConfig
logger.warning("A")
# Let's turn it off
logger.propagate = False
# Now it's handled by lastResort formatter
logger.warning("A")
# We can turn it off as well
logging.lastResort = False

logger.warning("A")  # No handlers could be found for logger "__main__"
