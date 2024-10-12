from EmotionRecognition.exception import CustomException
from EmotionRecognition.logger import logging
import sys

if __name__=="__main__":
    try:
        result = 5/2
        print(result)
        logging.info("program runs successfully")
        logging.info("welcome to our new project")
    except Exception as e:
        raise CustomException(e,sys)