from typing import Union


from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from typing import  List, Optional
from pydantic import BaseModel

from InstructorEmbedding import INSTRUCTOR

class Item(BaseModel):
    text: str
    vector: Optional[List[float]] = None


model = INSTRUCTOR('hkunlp/instructor-base')
# model = INSTRUCTOR('hkunlp/instructor-base').cuda()
instruction = "Represent this phrase for for retrieval:"

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
    embeddings = model.encode([[instruction,item.text]])
    item.vector = embeddings[0].tolist()

    return item

