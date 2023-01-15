from typing import Union
from enum import Enum

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get('/')
async def main():
    return {'message': 'Hello world'}


@app.get("/message/{some_message}")
async def get_message(some_message: str):
    return some_message


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: str | None = None, short: bool = False):
    item = {"item_id": item_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item


@app.put("/read_item/{item_id}")
async def read_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price}


@app.post("/post_mes/{post_message}")  # http://127.0.0.1:8000/post_mes/Wow i found you!
async def post_message(post_message: str):
    print(post_message)
    return {"post_message": post_message}


@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):
    if model_name is ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    return {"model_name": model_name, "message": "Have some residuals"}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
