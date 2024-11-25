import os
import sys


from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig,DataValidationConfig
from src.entity.config_entity import TrainingPipelineConfig

from src.logging.logger import logging
from src.exception.exception import CustomException

from src.components.data_validation import DataValidation

if __name__=="__main__":
    try:
        
        trainpipelineconfig = TrainingPipelineConfig()
        dataingestionconfig = DataIngestionConfig(trainpipelineconfig)
        data_ingestion = DataIngestion(dataingestionconfig)
        logging.info("Data ingestion started")
        data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
        print(data_ingestion_artifact)
        logging.info("Data ingestion Completed")

        data_validation_config = DataValidationConfig(trainpipelineconfig)
        data_validation = DataValidation(data_ingestion_artifact,data_validation_config)
        logging.info("Data validation started")
        data_validation_artifact = data_validation.initiate_data_validation()
        print(data_validation_artifact)
        logging.info("Data validation completed")


    except Exception as e:
        raise CustomException(e,sys)
