from fastapi import FastAPI
from typing import Union

app = FastAPI()

item = [{"item_name": "chung"}, {"item_name": "taek"}, {"item_name": "won"}]

@app.get("/items/")
async def read_items(start: int = 0, end: int = 3):
    return item[start: start + end]     # list slicing from parameters


@app.get("/items/{item_id}")
async def read_item(item_id: str, q: Union[str, None] = None):
    if q:
        return {"item_id": item_id, "q": q}
    
    return {"item_id": item_id}


@app.get("/users/{user_id}/items/{item_id}")        # variable q and short can add using {{ ?q="hihi"&short=True }}  
async def read_user_item(                           # next to thr url
    user_id: int, item_id: str, q: Union[str, None] = None, short: bool = False
):
    item = {"item_id": item_id, "owner_id": user_id}
    if q:
        item.update({"q": q})
    if not short:
        item.update(
            {"description": "This is an amazing item that has a long description"}
        )
    return item