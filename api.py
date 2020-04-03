from datetime import datetime

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel

from fastapi.staticfiles import StaticFiles


fake_db = {}

class Item(BaseModel):
    left: str
    right: str
    decision: str
    timestamp: str

app = FastAPI()

@app.get("/")
async def root():
    fake_db

@app.post("/items/{id}")
def update_item(id: str, item: Item):
    json_compatible_item_data = jsonable_encoder(item)
    fake_db[id] = json_compatible_item_data
    fake_db

app.mount("/static", StaticFiles(directory="static"), name="static")
