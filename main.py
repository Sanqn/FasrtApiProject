from typing import Union

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


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
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/read_item/{item_id}")
async def read_item(item_id: int, item: Item):
    return {"item_id": item_id, "item_name": item.name, "item_price": item.price}


@app.post("/post_mes/{post_message}")  # http://127.0.0.1:8000/post_mes/Wow i found you
async def post_message(post_message: str):
    print(post_message)
    return {"post_message": post_message}

@app.get("/users")
async def read_users():
    return ["Rick", "Morty"]


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
