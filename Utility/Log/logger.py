"""
logger utility
"""
import logging.handlers
import os
import time
import datetime

class Logger(object):
    """
    Contain method for logger class
    """
    def __init__(self, config):
        """
        :param config:
        """
        ts = time.time()

        service_name = config["service_name"] # service_name: mt_main
        log_file_path = config["path"]["log_path"] + service_name  # log_path: C:\LOGS\MatchingTool\mt_main
        if not os.path.isdir(log_file_path):
            os.makedirs(log_file_path)

        log_file = log_file_path + "/" + service_name   # log_path: C:\LOGS\MatchingTool\mt_main/mt_main
        self.log_obj = logging.getLogger(service_name)
        #hdlr_uploader = logging.FileHandler(log_file + "_" + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H%M%S')+'.log')
        #hdlr_service = logging.FileHandler(log_file + "_" + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d_%H%M%S')+'.log')
        formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', "%Y-%m-%d %H:%M:%S")
        #hdlr_uploader.setFormatter(formatter)
        #hdlr_service.setFormatter(formatter)
        # adding Rotating file handler
        logHandler = logging.handlers.TimedRotatingFileHandler(filename=str(log_file), backupCount=2, when='M', interval=600)
        logHandler.setLevel(config["log_level"])
        logHandler.setFormatter(formatter)



        self.log_obj.addHandler(logHandler)
        self.log_obj.setLevel(config["log_level"])
        self.log_obj.debug('Logger Initialized')
        #print(str(self.log_obj))

    @staticmethod
    def sample():
        return

    @staticmethod
    def demo():
        return