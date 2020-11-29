from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

import pandas as pd

dataTable = pd.read_table('/app/signatures.tsv').rename(columns={'Unnamed: 0': 'id'})
idList = dataTable['id'].to_list()

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"API is ready"}


@app.get('/getAllData')
def get_all_data():
    return dataTable.T


@app.get('/getIDList')
def get_id_list():
    return idList


@app.get('/getData/{item_id}')
def get_data(item_id: str):
    idList.index(item_id)
    index = idList.index(item_id)
    return dataTable.iloc[index]
