#!/usr/bin/env python3


import logging
import logging.config
logging.config.fileConfig('logging.conf')
logger = logging.getLogger(__name__)



logger.info('this is info')
logger.debug('this is debug')