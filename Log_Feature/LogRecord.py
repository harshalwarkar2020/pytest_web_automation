import os
import inspect
import logging
# Log_path = os.path.join(dir_path, "logfile.log")

dir_path = os.path.dirname(os.path.realpath(__file__))
Log_path = os.path.join(dir_path)



class LogData:
    def getLogger(self):
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        logsone = logging.FileHandler(Log_path+"logfile.log")
        formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
        logsone.setFormatter(formatter)

        logger.addHandler(logsone)

        logger.setLevel(logging.DEBUG)
        return logger














        # logger.debug("A debug statement is executed")
        # logger.info("Information statement")
        # logger.warning("warning")
        # logger.error("ERROR")
        # logger.critical("critical issue")