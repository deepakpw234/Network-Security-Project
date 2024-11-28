import os
import sys

from src.exception.exception import CustomException
from src.logging.logger import logging

from src.components.data_ingestion import DataIngestion
from src.components.data_validation import DataValidation
from src.components.data_transformation import DataTransformation
from src.components.model_training import ModelTrainer

from src.entity.config_entity import (TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig,
                                      DataTransformationConfig, ModelTrainerConfig)

from src.entity.artifact_entity import (DataIngestionartifact, DataValidationartifact, DataTransformationArtifact,
                                        ClassificationMetricArtifact, ModelTrainerArtifact)

from src.cloud.aws_syncer import S3Sync
from src.constant.training_pipeline import TRAINING_BUCKET_NAME

class TrainingPipeline:
    def __init__(self):
        self.train_pipeline_config = TrainingPipelineConfig()
        self.s3_sync = S3Sync()


    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.train_pipeline_config)
            logging.info("Start data ingestion")
            data_ingestion = DataIngestion(self.data_ingestion_config)
            data_ingestion_artifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"data ingestion completed and data artifact: {data_ingestion_artifact}")
            return data_ingestion_artifact

        except Exception as e:
            raise CustomException(e.sys)
        
    def start_data_validation(self, data_ingestion_artifact:DataIngestionartifact):
        try:
            self.data_validation_config = DataValidationConfig(training_pipeline_config=self.train_pipeline_config)
            logging.info("Start data validation")
            data_validation = DataValidation(data_ingestion_artifact=data_ingestion_artifact,data_validation_config=self.data_validation_config)
            data_validation_artifact = data_validation.initiate_data_validation()
            logging.info(f"data validation completed and data artifact: {data_validation_artifact}")
            return data_validation_artifact
        except Exception as e:
            raise CustomException(e,sys)
        
    def start_data_transformation(self, data_validation_artifact:DataValidationartifact):
        try:
            self.data_transforamtion_config = DataTransformationConfig(training_pipeline_config=self.train_pipeline_config)
            logging.info("Start data transformation")
            data_transformation = DataTransformation(data_validation_artifact=data_validation_artifact,data_transformation_config=self.data_transforamtion_config)
            data_transformation_artifact = data_transformation.initiate_data_transformation()
            logging.info(f"data transformation completed and data artifact: {data_transformation_artifact}")
            return data_transformation_artifact

        except Exception as e:
            raise CustomException(e,sys)
        
    def start_model_trainig(self, data_transformation_artifact:DataTransformationArtifact):
        try:
            self.model_trainer_config = ModelTrainerConfig(training_pipeline_config=self.train_pipeline_config)
            logging.info("Start model trainer")
            model_trainer = ModelTrainer(data_transformation_artifact=data_transformation_artifact,model_trainer_config=self.model_trainer_config)
            model_trainer_artifact = model_trainer.initiate_model_training()
            logging.info(f"Model trainer completed and data artifact: {model_trainer_artifact}")
            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e,sys)
        
    # Local artifact to aws s3 bucket
    # def sync_artifact_dir_to_s3(self):
    #     try:
    #         aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.train_pipeline_config.timestamp}"
    #         self.s3_sync.syn_folder_to_s3(folder=self.train_pipeline_config.artifact_dir,aws_bucket_url=aws_bucket_url)

    #     except Exception as e:
    #         raise CustomException(e,sys)
        
    # def sync_saved_model_dir_to_s3(self):
    #     try:
    #         aws_bucket_url = f"s3://{TRAINING_BUCKET_NAME}/artifact/{self.train_pipeline_config.timestamp}"
    #         self.s3_sync.syn_folder_to_s3(folder=self.train_pipeline_config.model_dir,aws_bucket_url=aws_bucket_url)

    #     except Exception as e:
    #         raise CustomException(e,sys)

    
        
    def run_pipeline(self):
        try:
            data_ingestion_artifact = self.start_data_ingestion()
            data_validation_artifact = self.start_data_validation(data_ingestion_artifact=data_ingestion_artifact)
            data_transformation_artifact = self.start_data_transformation(data_validation_artifact=data_validation_artifact)
            model_trainer_artifact = self.start_model_trainig(data_transformation_artifact=data_transformation_artifact)
            
            # self.sync_artifact_dir_to_s3()
            # self.sync_saved_model_dir_to_s3()

            return model_trainer_artifact

        except Exception as e:
            raise CustomException(e,sys)