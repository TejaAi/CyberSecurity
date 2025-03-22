import os
import sys
from dotenv import load_dotenv
load_dotenv()
import json

from pymongo.mongo_client import MongoClient






mongodb_url = os.getenv("mongodb_url")
print(mongodb_url)

import certifi
ca = certifi.where()

import pandas as pd
import numpy as np
import pymongo

from cybersecurity.exception.exception import CyberSecurity
from cybersecurity.logging.logger import logging


class CyberDataExtract():
    def __init__(self):
        try:
            pass
        except Exception as e:
            raise CyberSecurity(e,sys)
        

    def cv_to_json(self,file_path):
        try:
            data = pd.read_csv(file_path)
            data = data.reset_index(drop=True)
            return list(json.loads(data.T.to_json()).values())
        except Exception as e:
            raise CyberSecurity(e,sys)
        
    def insert_data_mongodb(self,records,database,collection):
        try:
            self.database = database
            self.records = records
            self.collection = collection
            self.mongo_client = MongoClient(mongodb_url)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]
            self.collection.insert_many(self.records)
            return (len(self.records))
        except Exception as e:
            raise CyberSecurity(e,sys)
        
if __name__ == '__main__':
    File_path = r"D:\CyberSecurity\cyberdata\phisingData.csv"
    Database = "TEJA"
    Collection ="NetworkData"
    networkobj = CyberDataExtract()
    records = networkobj.cv_to_json(file_path=File_path)
    print(records)
    no_of_records = networkobj.insert_data_mongodb(records,Database,Collection)
    print(no_of_records)

