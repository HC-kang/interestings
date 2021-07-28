from typing import Optional

from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder

app = FastAPI()

@app.get("/")
async def read_root():
    return "Hi"

from fastapi.encoders import jsonable_encoder

@app.put("/items/languges")
def update_item(
    item_id: int, name: Optional[str], design: Optional[str], init: Optional[int]
):
    return languages.append(
        {"id": item_id, "name": name, "designed_by": design, "first_appeared": init}
    )



@app.get("/items/languges/{item_id}")
async def get_language(item_id: int):
    result = {}

    for lang in languages:
        if lang["id"] == item_id:
            result = jsonable_encoder({"language": lang})
            break

    return result




languages = [
    {
        "id": 0,
        "name": "Python",
        "designed_by": "Guido van Rossum",
        "first_appeared": 1991,
    },
    {"id": 1, "name": "Java", "designed_by": "James Gosling", "first_appeared": 1995},
]

