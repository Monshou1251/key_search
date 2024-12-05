from enum import Enum

from fastapi import FastAPI

app = FastAPI()



@app.get("/{position}")
async def get_model(position):
    return {"selectedPostion": position}

