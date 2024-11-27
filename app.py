import os
import sys

from src.exception.exception import CustomException
from src.logging.logger import logging
from src.pipelines.train_pipeline import TrainingPipeline

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()

mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,requests,UploadFile,File
from fastapi.responses import Response
from uvicorn import run as app_run
from starlette.responses import RedirectResponse
import pandas as pd

client = pymongo.MongoClient(mongo_db_url,tlsCAFile=ca)

from src.constant.training_pipeline import DATA_INGESTION_DATABASE_NAME, DATA_INGESTION_COLLECTION_NAME

database = client[DATA_INGESTION_DATABASE_NAME]
collection = database[DATA_INGESTION_COLLECTION_NAME]

app = FastAPI()
origin = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins = origin,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"],
)

@app.get("/",tags=["authentication"])
async def index():
    return RedirectResponse(url="/docs")


@app.get("/train")
async def train_route():
    try:
        train_pipeline = TrainingPipeline()
        train_pipeline.run_pipeline()
        return Response("Training is successful")

    except Exception as e:
        raise CustomException(e,sys)
    

if __name__=="__main__":
    app_run(app,host="loacalhost",port=8000)