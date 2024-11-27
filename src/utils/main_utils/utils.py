import os
import sys
import pandas as pd
import numpy as np

from src.exception.exception import CustomException
from src.logging.logger import logging

from sklearn.model_selection import GridSearchCV
from sklearn.metrics import r2_score


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
    

def load_pickle_object(file_path:str):
    try:
        logging.info("pickle object is loading")
        if not os.path.exists(file_path):
            print(f"{file_path} path is not avaiable")
        with open(file_path,"rb") as file:
            return pickle.load(file)

    except Exception as e:
        raise CustomException(e,sys)

def load_numpy_array(file_path:str):
    try:
        logging.info("Numpy array is loading")
        if not os.path.exists(file_path):
            print(f"{file_path} path is not available")
        with open(file_path,"rb") as file:
            return np.load(file)

    except Exception as e:
        raise CustomException(e,sys)
    

def get_evaluate(x_train,y_train,x_test,y_test,models,params):
    try:
        report = {}
        for i in range(len(models.values())):
            model = list(models.values())[i]
            para = params[list(params.keys())[i]]

            gs = GridSearchCV(model,param_grid=para,cv=3)
            gs.fit(x_train,y_train)

            model.set_params(**gs.best_params_)
            model.fit(x_train,y_train)

            y_train_pred = model.predict(x_train)

            y_test_pred = model.predict(x_test)

            train_model_score = r2_score(y_train,y_train_pred)

            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]]=test_model_score


        return report


    except Exception as e:
        raise CustomException(e,sys)
    




