from fastapi import FastAPI, Body
from typing_extensions import Any
import json

app = FastAPI()


@app.get("/get_month")
async def get_month():
    with open("К0109-24.json", "r") as fp:
        return json.load(fp)

@app.post("/set_schedule")
async def set_schedule(payload: Any = Body(None)):
    with open("К0109-24.json", "w") as fp:
        json.dump(payload, fp)
    return payload