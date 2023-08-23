from enum import Enum
from fastapi import FastAPI


class ModelName(str, Enum):
    taek = "won"
    won = "taek"
    taekwon = "taekwon"

app = FastAPI()


@app.get("/models/{model_name}")
async def get_model(model_name: ModelName): # model_name: str also works. let me know the diff
    if model_name is ModelName.taekwon:
        return {"model_name": model_name, "message": "taekwon Learning FastAPI"}
    
    if model_name is ModelName.won:
        return {"model_name": model_name, "message": "won Learning FastAPI"}
    
    return {"model_name": model_name, "message": "taek Learning FastAPI"}


# for the path in path

@app.get("/files/{file_path:path}")     # parameter should match to any path
async def read_file(file_path: str):    # even if the path includes slashes(/)
    return {"file_path": file_path}