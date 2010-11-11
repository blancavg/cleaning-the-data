#!/usr/bin/python
############################################
### File:	logc.py
### Author:	Blanca A. Vargas-Govea
### Email:	blanca.vg@gmail.com
### Date:	10-Nov-2010
### ./logger.py
############################################
# http://docs.python.org/library/logging.html
# http://www.5dollarwhitebox.org/drupal/node/56
# http://docs.python.org/release/2.5.2/lib/logging-config-fileformat.html
# http://antonym.org/2005/03/a-real-python-logging-example.html

import logging
import sys, os

LOG_FILENAME = '../reports/log.txt'

# create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# create console handler and set level to debug
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)

# create file handler and set level to debug
if os.path.exists(os.path.dirname(LOG_FILENAME)):
    fh = logging.FileHandler(LOG_FILENAME,'w')
    fh.setLevel(logging.DEBUG)
else:
    print "Log directory does not exist" 
    sys.exit(1)

# create formatter
ch_formatter = logging.Formatter("%(levelname)s\t - %(message)s")
fh_formatter = logging.Formatter("%(asctime)s\t - %(levelname)s\t - %(message)s")

# add formatter to ch
ch.setFormatter(ch_formatter)
fh.setFormatter(fh_formatter)

# add ch and fh to logger
logger.addHandler(ch)
logger.addHandler(fh)

# "application" code
# logger.debug("debug message")
# logger.info("info message")
# logger.warn("warn message")
# logger.error("error message")
# logger.critical("critical message")

