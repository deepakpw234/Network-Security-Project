import os
import sys
import pandas as pd
import numpy as np

from src.exception.exception import CustomException
from src.logging.logger import logging

from src.constant.training_pipeline import TARGET_COLUMN
from src.constant.training_pipeline import DATA_TRANSFORMATION_IMPUTER_PARAMS

from src.entity.config_entity import DataTransformationConfig

from src.entity.artifact_entity import DataValidationartifact, DataTransformationArtifact

from src.utils.main_utils.utils import save_numpy_array,save_pickle_obj

from sklearn.impute import KNNImputer
from sklearn.pipeline import Pipeline

class DataTransformation:
    def __init__(self,data_validation_artifact:DataValidationartifact,
                 data_transformation_config:DataTransformationConfig):
        try:
            logging.info("Data Transfomation class is initiated with init constructor")
            self.data_validation_artifact = data_validation_artifact
            self.data_transformation_config = data_transformation_config

        except Exception as e:
            raise CustomException(e,sys)
        
    @staticmethod    
    def read_dataframe(file_path:str)->pd.DataFrame:
        try:
            return pd.read_csv(file_path)

        except Exception as e:
            raise CustomException(e,sys)
        
    def get_data_transformer_object(cls)->Pipeline:
        try:
            imputer = KNNImputer(**DATA_TRANSFORMATION_IMPUTER_PARAMS)

            preprocessor = Pipeline([("imputer",imputer)])

            return preprocessor
        
        except Exception as e:
            raise CustomException(e,sys)
        
    
    def initiate_data_transformation(self)->DataTransformationArtifact:
        try:
            logging.info("Initiate the data transformation with initiate function")
            train_df = self.read_dataframe(self.data_validation_artifact.valid_train_file_path)
            test_df = self.read_dataframe(self.data_validation_artifact.valid_test_file_path)

            # Creating the training dataframe into input features and target features
            input_feature_train_df = train_df.drop(TARGET_COLUMN,axis=1)
            target_feature_train_df = train_df[TARGET_COLUMN]
            target_feature_train_df = target_feature_train_df.replace(-1,0)
            logging.info("Input and target columns created for training dataframe")

            # Creating the test dataframe into input features and target features
            input_feature_test_df = test_df.drop(TARGET_COLUMN,axis=1)
            target_feature_test_df = test_df[TARGET_COLUMN]
            target_feature_test_df = target_feature_test_df.replace(-1,0)
            logging.info("Input and target columns craeted for test dataframe")

            preprocessor = self.get_data_transformer_object()

            transformed_input_train_feature = preprocessor.fit_transform(input_feature_train_df)
            transformed_input_test_feature = preprocessor.transform(input_feature_test_df)
            

            train_arr = np.c_[transformed_input_train_feature,np.array(target_feature_train_df)]
            test_arr = np.c_[transformed_input_test_feature,np.array(target_feature_test_df)]

            # Saving numpy array
            save_numpy_array(self.data_transformation_config.transformed_train_file_path,train_arr)
            save_numpy_array(self.data_transformation_config.transformed_test_file_path,test_arr)

            # Saving preprocessor object
            save_pickle_obj(self.data_transformation_config.transformed_object_file_path,preprocessor)

            # preparing the artifacts

            data_transformation_artifact = DataTransformationArtifact(
                transformed_object_file_path=self.data_transformation_config.transformed_object_file_path,
                transformed_train_file_path=self.data_transformation_config.transformed_train_file_path,
                transformed_test_file_path=self.data_transformation_config.transformed_test_file_path
            )

            return data_transformation_artifact



        except Exception as e:
            raise CustomException(e,sys)