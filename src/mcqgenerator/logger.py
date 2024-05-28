import logging
import os 
from datetime import datetime

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")

os.mkdir(log_path,exist_ok=True)


LOG_FILEPATH=os.path(log_path,LOG_FILE)
logging.basicConfig(
    level=logging.INFO,  # Change to DEBUG, WARNING, ERROR, or CRITICAL as needed
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')


