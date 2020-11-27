from fastapi import FastAPI, Query
from schemas import Book
from typing import List

app = FastAPI()

@app.post('/book')
def create_book(item: Book):
    return item

@app.get('/book')
def get_book(q: List[str] = Query(..., description="Search book")):
    return q
