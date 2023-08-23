from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}") # also can use async in front of the function
async def read_item(item_id: int, q: Union[str, None] = None): # => same with {{ q: str }} whats the diff? 
    return {"item_id": item_id, "q": q}                        # A. if you don't declare default: none,
                                                               # variable q is no longer optional

@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


# path evaluated in order # 1

@app.get("/users/me")       # if you wanna use static path in dynamic url like "/users/{user_id}"
async def read_user_me():   # you have to declare the static first
    return {"user_id": "current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}


# path evaluated in order # 2

@app.get("/same_path")      # if you enter "/same_path"
async def same_path1():     # you probably run the first function. because of the logic of FastAPI
    return ["first", "path"]


@app.get("/same_path")
async def same_path2():
    return ["second", "path"]
