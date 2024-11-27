import os
import sys
import pandas as pd
import numpy as np


'''
Defining common constant variable for training pipeline
'''
TARGET_COLUMN = "Result"
PIPELINE_NAME: str = "NetworkSecurity"
ARTIFACT_DIR: str = "artifacts"
FILE_NAME: str = "phisingData.csv"

TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

SCHEMA_FILE_PATH = os.path.join("data_schema","schema.yaml")

PROCESSING_OBJECT_FILE_PATH = "preprocessing.pkl"

SAVED_MODEL_DIR = "saved_model"
MODEL_FILE_NAME = "model.pkl"


'''
Data Ingestion related constant start with DATA_INGESTION Var Name
'''

DATA_INGESTION_DATABASE_NAME: str = 'Deeapk'
DATA_INGESTION_COLLECTION_NAME: str = 'Network_data'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_NAME: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR_NAME: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



'''
Data Validation related constant start with data validation
'''

DATA_VALIDATION_DIR_NAME:str = "data_validation"
DATA_VALIDATION_VALID_DIR:str = "validated"
DATA_VALIDATION_INVALID_DIR:str = "invalid"
DATA_VALIDATION_DRIFT_REPROT_DIR:str = "drift_report"
DATA_VALIDATION_DRIFT_REPROT_FILE_NAME:str = "report.yaml"


'''
Data transformation related constant start with data transformation
'''
DATA_TRANSFORMATION_DIR_NAME:str = "data_transformation"
DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR:str = "transformed"
DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR:str = "transformed_object"


### knn imputer
DATA_TRANSFORMATION_IMPUTER_PARAMS = {
    "missing_values":np.nan,
    "n_neighbors":3,
    "weights":"uniform",
}


'''
Model trainer realted constant strat with model trainer
'''
MODEL_TRAINER_DIR_NAME:str = "model_trainer"
MODEL_TRAINER_TRAINED_MODEL_DIR:str = "trained_model"
MODEL_TRAINER_TRAINED_MODEL_NAME:str = "model.pkl"
MODEL_TRAINER_EXPECTED_SCORE:float = 0.6
MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD:float = 0.05


'''
Constant for local to s3 bucket
'''
TRAINING_BUCKET_NAME = "networksecurity234"