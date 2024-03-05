from us_visa.logger import logging
from us_visa.exceptions import USvisaException
import sys

logging.info("Welcome to our custom logging.")



try:
    a= 1/"10"

except Exception as e:
    logging.exception(e)
    raise USvisaException(e,sys)

