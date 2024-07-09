import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_dir = os.path.join(os.getcwd(),"logs")
os.makedirs(log_dir,exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(log_dir,LOG_FILE)

#Always need to configure
logging.basicConfig(
    filename = LOG_FILE_PATH,
    format = "[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    #only messages with this level or higher will be logged
    level = logging.INFO
)

