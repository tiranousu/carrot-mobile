from fastapi import FastAPI, UploadFile, Form, Response
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from fastapi_login.exceptions import InvalidCredentialsException
from typing import Annotated
import sqlite3

con = sqlite3.connect('db.db', check_same_thread=False)
cur = con.cursor()

app = FastAPI()

SERCRET = "super-coding"
manager = LoginManager(SERCRET,'/login')

@manager.user_loader()
def query_user(id):
    con.row_factory = sqlite3.Row
    cur = con.cursor()
    user = cur.execute(f"""
                       SELECT * from user WHERE id = '{id}'
                       """).fetchone()
    return user

@app.post('/login')
def login(id:Annotated[str,Form()], 
           password:Annotated[str,Form()]):
    user = query_user(id)
    if not user:
        raise InvalidCredentialsException
    elif password != user['password']:
        raise InvalidCredentialsException
    
    access_token = manager.create_access_token(data={
        'myname':'hi!'
    })
    
    return {'access_token':access_token}


@app.post('/signup')
def signup(id:Annotated[str,Form()], 
           password:Annotated[str,Form()],
           name:Annotated[str,Form()],
           email:Annotated[str,Form()]):
    
    #TODO : 이미 가입되어 있는 회원인지 체크
    cur.execute(f"""
                INSERT INTO user(id,name,email,password)
                VALUES ('{id}','{name}','{email}','{password}' )
                """)
    con.commit()
    return '200'

@app.post('/items')
async def create_itme(image:UploadFile, 
                 title:Annotated[str, Form()], 
                 price:Annotated[int, Form()], 
                 description:Annotated[str, Form()],
                 place:Annotated[str, Form()],
                 insertAt:Annotated[int, Form()]
                 ):
    
    image_bytes = await image.read()
    cur.execute(f"""
                INSERT INTO items(title,image,price,description,place,insertAt)
                VALUES ('{title}','{image_bytes.hex()}',{price},'{description}','{place}',{insertAt})
                """)
    con.commit()
    
    return '200'

@app.get('/items')
async def get_items():
    con.row_factory = sqlite3.Row #컬럼명도 같이 가져오게 처리
    cur = con.cursor()
    rows = cur.execute(f"""
                       SELECT * FROM items
                       """).fetchall()
    
    return JSONResponse(jsonable_encoder(dict(row) for row in rows))

@app.get('/images/{item_id}')
async def get_image(item_id):
    cur = con.cursor() #16진법을 2진법으로
    image_bytes = cur.execute(f"""
                              SELECT image From items WHERE id={item_id}
                              """).fetchone()[0]
    return Response(content=bytes.fromhex(image_bytes), media_type='image/*')

app.mount("/", StaticFiles(directory="frontend", html=True), name="frontend")