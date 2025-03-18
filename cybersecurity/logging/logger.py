import os
import logging
from datetime import datetime


log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)
log_path = os.path.join(log_path,log_file_name)

logging.basicConfig(
    filename=log_path,
    format='[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)