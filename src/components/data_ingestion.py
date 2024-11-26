import os
import sys
import pandas as pd
import numpy as np
import pymongo

from src.exception.exception import CustomException
from src.logging.logger import logging

from src.entity.config_entity import DataIngestionConfig
from src.entity.artifact_entity import DataIngestionartifact
from sklearn.model_selection import train_test_split


from dotenv import load_dotenv
load_dotenv()

MONGO_DB_URL = os.getenv("MONGO_DB_URL")

class DataIngestion:
    def __init__(self,data_ingestion_config:DataIngestionConfig):
        try:
            logging.info("Data Ingestion constructor initaited")
            self.data_ingestion_config = data_ingestion_config
        except Exception as e:
            raise CustomException(e,sys)

    def export_collection_to_dataframe(self):
        try:
            database_name = self.data_ingestion_config.database_name
            collection_name = self.data_ingestion_config.collection_name

            self.mango_client = pymongo.MongoClient(MONGO_DB_URL)
        
            collection = self.mango_client[database_name][collection_name]
            
            df = pd.DataFrame(list(collection.find()))
            
            if "_id" in list(df.columns):
                df.drop("_id",axis=1,inplace=True)
            
            df.replace({"na":np.nan},inplace=True)

            return df

        except Exception as e:
            raise CustomException(e,sys)
        
    def export_data_into_feature_store(self,dataframe):
        try:
            feature_store_file_path = self.data_ingestion_config.feature_store_file_path
            # creating folder
            os.makedirs(os.path.dirname(feature_store_file_path),exist_ok=True)

            dataframe.to_csv(feature_store_file_path, index=False,header=True)

            return dataframe

        except Exception as e:
            raise CustomException(e,sys)

    def data_into_train_test_split(self,dataframe):
        try:
            
            train_set, test_set = train_test_split(dataframe,test_size=self.data_ingestion_config.train_test_split_ratio,random_state=42)

            # Saving train_set into the ingested directory

            training_file_path = self.data_ingestion_config.training_file_path
            os.makedirs(os.path.dirname(training_file_path),exist_ok=True)

            train_set.to_csv(training_file_path,index=False,header=True)

            # Saving test_set into the ingested directory

            testing_file_path = self.data_ingestion_config.testing_file_path
            os.makedirs(os.path.dirname(testing_file_path),exist_ok=True)

            test_set.to_csv(testing_file_path,index=False,header=True)

        except Exception as e:
            raise CustomException(e,sys)

    def initiate_data_ingestion(self):
        try:
            logging.info("Calling data from mongo DB")
            dataframe = self.export_collection_to_dataframe()
            logging.info("MongoDB data is loaded into to dataframe")
            logging.info("Raw data saving in featuer store is started")
            dataframe = self.export_data_into_feature_store(dataframe)
            logging.info("Raw data is saved in feature store")
            logging.info("Train test split started")
            self.data_into_train_test_split(dataframe)
            logging.info("Train test completed and train and test csv's saved in ingested store")
            dataingestionartifact = DataIngestionartifact(train_file_path=self.data_ingestion_config.training_file_path,
                                                          test_file_path=self.data_ingestion_config.testing_file_path)
            
            logging.info("Train and test file path saved in the artifact")

            return dataingestionartifact
        except Exception as e:
            raise CustomException(e,sys)




