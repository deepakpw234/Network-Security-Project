import os
import sys
import json
from dotenv import load_dotenv

import pandas as pd
import numpy as np
import pymongo
import pymongo.mongo_client

from src.exception.exception import CustomException
from src.logging.logger import logging

load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

print(MONGO_DB_URL)

import certifi
ca = certifi.where()


class NetworkDataExtract:
    def  __init__(self):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
        

    def csv_to_json_convertor(self,file_path):
        try:
            data = pd.read_csv(file_path)

            data.reset_index(drop=True,inplace=True)

            records = list(json.loads(data.T.to_json()).values())

            print(records)

            return records

        except Exception as e:
            raise CustomException(e,sys)
        

    def insert_data_mongodb(self,records,database,collection):
        try:
            self.records = records
            self.database = database
            self.collection = collection

            self.mongo_client = pymongo.MongoClient(MONGO_DB_URL)
            self.database = self.mongo_client[self.database]
            self.collection = self.database[self.collection]

            self.collection.insert_many(self.records)

            return len(self.records)

        except Exception as e:
            raise CustomException(e,sys)



if __name__=="__main__":
    data_file_path = "artifacts\data\phisingData.csv"
    database = "Deeapk"
    collection = "Network_data"

    network_obj = NetworkDataExtract()
    records = network_obj.csv_to_json_convertor(data_file_path)
    print(records)
    no_of_record = network_obj.insert_data_mongodb(records,database,collection)
    print(no_of_record)



















# from pymongo.mongo_client import MongoClient

# uri = "mongodb+srv://deepakpw234:admin123@cluster0.5xhgy.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# # Create a new client and connect to the server
# client = MongoClient(uri)

# # Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)