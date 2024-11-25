import os
import sys
import pandas as pd
import numpy as np

from src.exception.exception import CustomException
from src.logging.logger import logging


import yaml
import dill
import pickle


def read_yaml_file(file_path:str)-> dict:
    try:
        with open(file_path,"rb") as yaml_file:
            return yaml.safe_load(yaml_file)

    except Exception as e:
        raise CustomException(e,sys)
    

def write_yaml_file(file_path:str, content:object, replace:bool=False):
    try:
        if replace:
            if os.path.exists(file_path):
                os.remove(file_path)
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"w") as yaml_file:
            yaml.dump(content,yaml_file)

    except Exception as e:
        raise CustomException(e,sys)
