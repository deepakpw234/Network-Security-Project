import os
import sys


from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig

from src.logging.logger import logging
from src.exception.exception import CustomException

if __name__=="__main__":
    try:
        logging.info("Data ingestion started")
        trainpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        data_ingestion.initiate_data_ingestion()
        logging.info("Data ingestion Complated")
    except Exception as e:
        raise CustomException(e,sys)
