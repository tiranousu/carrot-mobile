from fastapi import FastAPI, UploadFile, Form, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from typing import Annotated
import sqlite3

con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

app = FastAPI()

@app.post("/signup")
def signup(id: Annotated[str, Form()],
           password: Annotated[str, Form()],
           name: Annotated[str, Form()],
           email: Annotated[str, Form()]):
    cur.execute("""
                INSERT INTO users(id, name, email, password)
                VALUES (?, ?, ?, ?)
                """, (id, name, email, password))
    con.commit()  # 'comit'을 'commit'으로 수정
    return "200"

@app.get('/items')
async def get_items():
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    rows = cur.execute("SELECT * FROM items").fetchall()
    return JSONResponse(content=jsonable_encoder([dict(row) for row in rows]))

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor()
    image_bytes = cur.execute("""
                              SELECT image FROM items WHERE id = ?
                              """, (item_id,)).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes))

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")
