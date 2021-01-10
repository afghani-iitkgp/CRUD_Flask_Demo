import logging
#import logging.handlers
import logging.handlers as handlers
#import logstash

from logstash_formatter import LogstashFormatter
logger = logging.getLogger(__name__)

# Set logging level across the logger. Set to INFO in production
logger.setLevel(logging.DEBUG)

# create formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
formatter1 = LogstashFormatter()
# LogstashLog Handler
#logstash_handler = logstash.LogstashHandler("54.69.130.37",9299, version=1)
#logstash_handler.setFormatter(formatter1)
#Local File Handler
#create file handler which logs even debug messages
file_handler = logging.FileHandler(__name__ + '_file.log')
file_handler.setLevel(logging.INFO)
file_handler.setFormatter(formatter)

# create console handler with debug level
# This should be changed to ERROR in production
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)
console_handler.setFormatter(formatter)

#adding Rotating file handler
logHandler = handlers.RotatingFileHandler('app.log', maxBytes=100, backupCount=2)
logHandler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

logHandler = logging.FileHandler(__name__ + '_file.log')
logHandler.setFormatter(formatter)


# add the handlers to the logger
#logger.addHandler(file_handler)
#logger.addHandler(console_handler)
logger.addHandler(logHandler)
#logger.addHandler(logstash_handler)