import os
import sys
from datetime import datetime

from src.exception.exception import CustomException
from src.logging.logger import logging


from src.constant import training_pipeline



# print(training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO)
# print(training_pipeline.PIPELINE_NAME)


class TrainingPipelineConfig:
    def __init__(self,timestamp = datetime.now()):
        timestamp = timestamp.strftime("%d_%m_%Y_%H_%M_%S")
        self.pipeline_name = training_pipeline.PIPELINE_NAME
        self.artifact_name = training_pipeline.ARTIFACT_DIR
        self.artifact_dir = os.path.join(self.artifact_name,timestamp)
        self.timestamp = timestamp
        # print(self.pipeline_name)
        # print(self.artifact_name)
        # print(self.artifact_dir)
        # print(self.timestamp)

        

class DataIngestionConfig:
    def __init__(self,training_pipeline_config:TrainingPipelineConfig):
        self.data_ingestion_dir = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_DIR_NAME)
        self.feature_store_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_NAME)
        self.training_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,training_pipeline.TRAIN_FILE_NAME)
        self.testing_file_path = os.path.join(self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTED_DIR_NAME,training_pipeline.TEST_FILE_NAME)
        self.train_test_split_ratio = training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO
        self.database_name = training_pipeline.DATA_INGESTION_DATABASE_NAME
        self.collection_name = training_pipeline.DATA_INGESTION_COLLECTION_NAME


        # print(self.data_ingestion_dir)
        # print(self.feature_store_file_path)
        # print(self.training_file_path)
        # print(self.testing_file_path)
        # print(self.train_test_split_ratio)
        # print(self.database_name)
        # print(self.collection_name)

class DataValidationConfig:
    def __init__(self, training_pipeline_config:TrainingPipelineConfig):
        self.data_validation_dir:str = os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str = os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str = os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.drift_report_file_path:str = os.path.join(self.data_validation_dir,training_pipeline.DATA_VALIDATION_DRIFT_REPROT_DIR,training_pipeline.DATA_VALIDATION_DRIFT_REPROT_FILE_NAME)




# if __name__=="__main__":

#     logging.info("logging start")
#     a = TrainingPipelineConfig()
#     b = DataIngestionConfig(a)