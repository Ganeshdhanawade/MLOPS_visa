from us_visa.logger import logging
from us_visa.exception import USvisaException
from us_visa.pipline.training_pipeline import TrainPipeline
import sys

obj = TrainPipeline()
obj.run_pipeline()

logging.info("the data ingesion is completed")

# try:
#     a =2/0
# except Exception as e:
#     raise USvisaException(e,sys)