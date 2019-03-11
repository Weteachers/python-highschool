import logging

#logging.basicConfig(level=logging.DEBUG)

LOG_FORMAT = "%(asctime)s=====%(levelname)s=====%(message)s"

logging.basicConfig(filename="tc.log", level=logging.DEBUG, format=LOG_FORMAT)

logging.debug("This is a debug log.")
logging.info("This is a info log.")
logging.warning("This is a warning log.")
logging.error("This is a error log.")
logging.critical("This is a critical log.")


# 另外一种写法
logging.log(logging.DEBUG, "This is a debug log.")
logging.log(logging.INFO, "This is a info bug.")
logging.log(logging.WARNING, "This is a warning bug.")
logging.log(logging.ERROR, "This is a error bug.")
logging.log(logging.CRITICAL, "This is a critical bug.")