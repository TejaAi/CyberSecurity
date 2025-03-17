import os
import logging
from datetime import datetime


log_file_name = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
log_path = os.path.join(os.getcwd(),"logs",log_file_name)
os.makedirs(log_path,exist_ok=True)

logging.basicConfig(
    filename=log_path,
    format='[ %(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s'
)