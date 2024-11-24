from src.components.data_ingestion import DataIngestion
from src.entity.config_entity import DataIngestionConfig
from src.entity.config_entity import TrainingPipelineConfig

from src.logging.logger import logging


if __name__=="__main__":
    logging.info("data_ingestion_started")

    trainpipelineconfig = TrainingPipelineConfig()
    logging.info("train_pipeline_work")
    dataingestionconfig = DataIngestionConfig(trainpipelineconfig)
    logging.info("data_ingestion_config_work")

    data_ingestion = DataIngestion(dataingestionconfig)
    logging.info("data_ingestion_work")

    data_ingestion.initiate_data_ingestion()
