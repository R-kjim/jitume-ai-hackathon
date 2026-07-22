from typing import AnyStr, Dict
from fastapi import HTTPException, Request, Response, status

from datetime import datetime, timezone, timedelta
from typing import Dict
from server.app.config.config import variables
from jose import jwt


JWT_SECRET_KEY= variables.jwt_secret_key
ALGORITHM = "HS256"

async def create_access_token(data: dict, expires_delta:datetime= timedelta(minutes=60)) -> Dict:
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    
    return {
        "access_token":jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM),
        "expires_at": expire
        }

async def create_refresh_token(data: dict, expires_delta:datetime= timedelta(days=120)) -> Dict:
    to_encode = data.copy()
    expire = datetime.now(tz=timezone.utc) + expires_delta
    to_encode.update({"exp": expire})
    return {
        "refresh_token": jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=ALGORITHM),
        "expires_at":expire
    }

async def revoke_token(data:Dict):
    data.update({"exp":datetime.now() - timedelta(seconds=2)})
    return jwt.encode(data, JWT_SECRET_KEY, algorithm=ALGORITHM)

async def verify_token(token: str):
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("user_id")
        if user_id is None:
            raise Exception("Invalid credentials")
        return user_id
    except Exception as e:
        raise Exception(str(e))

async def get_current_user( request: Request, response: Response) -> Dict[ AnyStr, any]:
    try:
        token = request.cookies.get("at_allow_me")
        user_id = None
        if not token:
            refresh_token = request.cookies.get("rt_allow_me")
            user_id = await verify_token(refresh_token)
            new_token = await create_access_token(
                data={
                    "user_id":str(user_id)
                }
            )
            response.set_cookie(
                key="at_allow_me",
                value=new_token["access_token"],
                expires= new_token["expires_at"],
                httponly=True,      
                secure=True,        
                samesite= "lax",     
                path = "/",
            )
        else:
            user_id = await verify_token(token)
        if not user_id:
            raise Exception("Access denied")
        return {"user_id": user_id}
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid access token",
            headers={"WWW-Authenticate": "Bearer"},
        )
    
