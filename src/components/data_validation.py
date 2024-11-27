import os
import sys
import pandas as pd

from src.exception.exception import CustomException
from src.logging.logger import logging


from src.entity.config_entity import DataValidationConfig
from src.entity.artifact_entity import DataIngestionartifact,DataValidationartifact
from scipy.stats import ks_2samp   # for checking the distribution


from src.constant.training_pipeline import SCHEMA_FILE_PATH
from src.utils.main_utils.utils import read_yaml_file, write_yaml_file


class DataValidation:
    def __init__(self,data_ingestion_artifact:DataIngestionartifact,
                 data_validation_config:DataValidationConfig):
        try:
            self.data_ingestion_artifact = data_ingestion_artifact
            self.data_validation_config = data_validation_config
            self._schema_config = read_yaml_file(SCHEMA_FILE_PATH)

        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod    
    def read_data(file_path)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def validate_no_of_columns(self,dataframe:pd.DataFrame)->bool:
        try:
            no_of_columns = len(self._schema_config['columns'])
            logging.info(f"required columns are {no_of_columns}")
            logging.info(f"dataframe has columns {len(dataframe.columns)}")

            if len(dataframe.columns) == no_of_columns:
                return True
            else:
                return False

        except Exception as e:
            raise CustomException(e,sys)
        
    def detect_dataset_drift(self,base_dataframe,current_dataframe,threshold=0.05)->bool:
        try:
            status = True
            report = {}
            for column in base_dataframe.columns:
                d1 = base_dataframe[column]
                d2 = current_dataframe[column]
                is_same_dist = ks_2samp(d1,d2)
                if threshold <= is_same_dist.pvalue:
                    is_found = False
                else:
                    is_found = True
                    status = False

                report.update({column:{
                    "p-value":float(is_same_dist.pvalue),
                    "drift_status": is_found
                }})

            drift_report_file_path = self.data_validation_config.drift_report_file_path

            # creating the directory
            dir_path = os.path.dirname(drift_report_file_path)
            os.makedirs(dir_path,exist_ok=True)

            write_yaml_file(file_path=drift_report_file_path,content=report)

            return status

        except Exception as e:
            raise CustomException(e,sys)
        

    def initiate_data_validation(self)->DataValidationartifact:
        try:
            train_file_path = self.data_ingestion_artifact.train_file_path
            test_file_path = self.data_ingestion_artifact.test_file_path

            # read data from train and test
            train_dataframe = DataValidation.read_data(train_file_path)
            test_datafrane = DataValidation.read_data(test_file_path)

            # validate number of columns
            status = self.validate_no_of_columns(train_dataframe)
            if status==False:
                print(f"Train dataframe does not contain all columns")        

            status = self.validate_no_of_columns(test_datafrane)
            if status==False:
                print(f"Test dataframe does not contain all columns")

            # check data drift
            status = self.detect_dataset_drift(train_dataframe,test_datafrane)
            dir_path = os.path.dirname(self.data_validation_config.valid_train_file_path)
            os.makedirs(dir_path,exist_ok=True)
            
            train_dataframe.to_csv(self.data_validation_config.valid_train_file_path,header=True,index=False)

            test_datafrane.to_csv(self.data_validation_config.valid_test_file_path,header=True,index=False)

            datavalidationartifact = DataValidationartifact(
                validation_status=status,
                valid_train_file_path=self.data_validation_config.valid_train_file_path,
                valid_test_file_path=self.data_validation_config.valid_test_file_path,
                invalid_train_file_path=None,
                invalid_test_file_path=None,
                drift_report_file_path=self.data_validation_config.drift_report_file_path
            )

            return datavalidationartifact

        except Exception as e:
            raise CustomException(e,sys)