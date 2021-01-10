"""
Purpose: Read the configurations from yaml file
"""
import yaml
from Utility import utility_file


# this method is to read the configuration from backup.conf

def read_configuration(file_name):
    """
    :param file_name:
    :return: all the configuration constants
    """
    with open(file_name, 'r') as stream:
        try:
            return yaml.load(stream, Loader=yaml.FullLoader)
        except yaml.YAMLError as exc:
            utility_file.logger.error("Configuration File Read Error " + str(file_name) + " Error" + str(exc))
