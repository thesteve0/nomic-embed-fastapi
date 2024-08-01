from typing import Union

import nomic
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import  List, Optional
from pydantic import BaseModel
from nomic import embed

class Item(BaseModel):
    text: str
    vector: Optional[List[float]] = None


embedder = nomic.embed

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World2"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

@app.post("/embed")
# @app.post("/embed", response_model=Item)
async def create_item(item: Item) -> Item:
    item.vector = embed.text(
        texts=[item.text],
        model='nomic-embed-text-v1.5',
        task_type='search_document',
        inference_mode='local',
    )
    return item

