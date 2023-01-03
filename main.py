from typing import Union

import uvicorn
from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def main():
    return {'hello': 'pop'}


@app.get("/items/{item_id}")
async def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)