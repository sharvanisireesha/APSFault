from sensor.logger import logging
from sensor.exception import SensorException
from sensor.utils import get_collection_as_dataframe
import sys,os

def test_logger_and_exception():
    try:
        logging.info("starting the logger and the exception")
        result = 3/0
        print(result)
        logging.info("stopping  the logger and the exception")
    except Exception as e:
        logging.debug(str(e))
        raise SensorException(e, sys)

if __name__ =="__main__":
    try:
        get_collection_as_dataframe(database_name ="aps", collection_name ="sensor")
    except Exception as e:
        print(e)