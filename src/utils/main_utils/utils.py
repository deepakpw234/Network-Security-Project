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
    

def save_numpy_array(file_path,array:np.array):
    try:
        logging.info("Saving into numpy array")
        dir_name = os.path.dirname(file_path)
        os.makedirs(dir_name,exist_ok=True)
        with open(file_path,"wb") as numpy_file:
            np.save(numpy_file,array)

    except Exception as e:
        raise CustomException(e,sys)
    
def save_pickle_obj(file_path,obj:object):
    try:
        logging.info("Preprocessor is saving into pickle object")
        os.makedirs(os.path.dirname(file_path),exist_ok=True)
        with open(file_path,"wb") as file_obj:
            pickle.dump(obj,file_obj)

    except Exception as e:
        raise CustomException(e,sys)
