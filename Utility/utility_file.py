import os
import __root__
from Config import configreader
from Utility.Log.logger import Logger

# Reading the configuration

config_file = os.path.join(__root__.path(), "./Config/service.yml")
config = configreader.read_configuration(config_file)
logger = Logger(config).log_obj
