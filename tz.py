from tinydb import TinyDB, Query
import uvicorn
from fastapi import FastAPI
import services
from typing import Union

app = FastAPI()
db = TinyDB("db.json")


@app.post("/get_form", response_model=Union[str, dict])
async def get_form(**data):
    form = services.find_form(data, db)


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
