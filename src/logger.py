import logging
import os
from datetime import datetime

#Name of the log file
LOG_FILE = f"{datetime.now().strftime('%m_%d_%y_%H_%M_%S')}.log"

#Path for the log file - store in the current working directory(cwd) with logs tag
logs_path = os.path.join(os.getcwd(),"logs",LOG_FILE)

#Creating the dir - if exist, append
os.makedirs(logs_path,exist_ok=True)

LOG_FILE_PATH = os.path.join(logs_path,LOG_FILE)

#Config info
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format = "[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

if __name__=='__main__':
    logging.info("Logging has started")
