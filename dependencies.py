from fastapi import Depends, HTTPException
from hashing import Token
from fastapi.security import OAuth2PasswordBearer

from config import authConfig

oauth2_schema = OAuth2PasswordBearer(tokenUrl=authConfig['TokenUrl'])


async def get_current_user(token: str = Depends(oauth2_schema)):
    try:
        result = Token.decode(token)
    except Exception as e:
        raise HTTPException(status_code=400, detail='token error')
    return result
