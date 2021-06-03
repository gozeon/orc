from fastapi import Depends
from hashing import Token
from fastapi.security import OAuth2PasswordBearer

from config import authConfig

print(authConfig['TokenUrl'])

oauth2_schema = OAuth2PasswordBearer(tokenUrl=authConfig['TokenUrl'])


async def get_current_user(token: str = Depends(oauth2_schema)):
    return Token.decode(token)
