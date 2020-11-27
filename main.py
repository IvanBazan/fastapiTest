from fastapi import FastAPI, Query
from schemas import Book
from typing import List
import pandas as pd

dataTable = pd.read_table('signatures.tsv').rename(columns={'Unnamed: 0': 'id'})
# pd.read_csv('signatures.tsv', sep='\t', index_col='Unnamed: 0')
# dataTable.loc[dataTable.id == 'NSCLC1352']

app = FastAPI()

@app.post('/book')
def create_book(item: Book):
    return item

@app.get('/book')
def get_book(q: List[str] = Query(..., description="Search book")):
    return q

@app.get('/getIDs')
def get_ids():
    return dataTable.loc[dataTable.id == 'NSCLC1352']

