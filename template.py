import os
import sys
from pathlib import Path


list_of_files = [
    "src/__init__.py",
    "src/exception.py",
    "src/logger.py",
    "src/utils.py",
    "src/components/__init__.py",
    "src/components/data_ingestion.py",
    "src/components/data_transformation.py",
    "src/components/model_training.py",
    "src/pipelines/__init__.py",
    "src/pipelines/train_pipeline.py",
    "src/pipelines/predict_pipeline.py",
    "artifacts/model/abc.txt",
    "artifacts/preprocessor/abc.txt",
    "artifacts/data/abc.txt",
    "notebook/abc.txt",
    "logs/abc.txt",
    "templates/index.html",
    "templates/home.html",
    "application.py",
    "Dockerfile",
    "README.md",
    ".gitignore",
    "setup.py",
    "LICENSE",

]



for file in list_of_files:
    file = Path(file)
    # print(file)

    dir_name , file_name = os.path.split(file)

    print(dir_name)
    print(file_name)

    if dir_name !="":
        os.makedirs(dir_name,exist_ok=True)

    if (not os.path.exists(file)) or (os.path.getsize(file)==0):
        with open(file,"w") as f:
            pass