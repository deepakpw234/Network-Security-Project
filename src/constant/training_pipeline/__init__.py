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


'''
Data Ingestion related constant start with DATA_INGESTION Var Name
'''

DATA_INGESTION_DATABASE_NAME: str = 'Deeapk'
DATA_INGESTION_COLLECTION_NAME: str = 'Network_data'
DATA_INGESTION_DIR_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_NAME: str = 'feature_store'
DATA_INGESTION_INGESTED_DIR_NAME: str = 'ingested'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2



