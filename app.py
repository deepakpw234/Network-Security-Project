import os
import sys

from src.exception.exception import CustomException
from src.logging.logger import logging
from src.pipelines.train_pipeline import TrainingPipeline
from src.utils.main_utils.utils import load_pickle_object

from src.utils.ml_utils.model.estimator import NetworkData

import certifi
ca = certifi.where()

from dotenv import load_dotenv
load_dotenv()

mongo_db_url = os.getenv("MONGO_DB_URL")
print(mongo_db_url)

import pymongo

from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI,Request,UploadFile,File
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

from fastapi.templating import Jinja2Templates
templates = Jinja2Templates(directory="./templates")


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
    
@app.post("/predict")
async def predict_route(request:Request,file:UploadFile = File(...)):
    try:
        df = pd.read_csv(file.file)
        # print(df)

        # loading preprocessor and model
        preprocessor = load_pickle_object('final_model/preprocessor.pkl')
        model = load_pickle_object('final_model/model.pkl')

        network_model = NetworkData(preprocessor=preprocessor,model=model)

        y_pred = network_model.predict(df)
        print(y_pred)
        df['predtiction'] = y_pred
        print(df['predtiction'])

        df.to_csv("prediction_output/output.csv")

        table_html = df.to_html(classes="table table-striped")
        # print(table_html)
        return templates.TemplateResponse("table.html", {"request":request,"table":table_html})
    

    except Exception as e:
        raise CustomException(e,sys)    

if __name__=="__main__":
    app_run(app,host="loacalhost",port=8000)