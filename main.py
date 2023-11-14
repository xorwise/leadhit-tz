from tinydb import TinyDB
import uvicorn
from fastapi import FastAPI, HTTPException, Request
import services
from typing import Union
import init_db

app = FastAPI()
db = TinyDB("db.json")


@app.post(
    "/get_form",
    description="Поиск шаблонов форм, по входной форме",
    response_model=Union[str, dict],
)
async def get_form(request: Request):
    data = dict(request.query_params)
    try:
        form = services.find_form(data, db)
        return form
    except HTTPException:
        template = services.create_template(data)
        return template


if __name__ == "__main__":
    init_db.init()
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
