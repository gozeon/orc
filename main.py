from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

from hashing import Token
from router import users

app = FastAPI()
app.include_router(users.router)


@app.post("/token", tags=['auth'])
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    return {"access_token": Token.encode(form_data.__dict__), "token_type": "bearer"}

