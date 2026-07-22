from  fastapi import APIRouter, Depends, HTTPException, Response, status
from pydantic import EmailStr

from server.app.config.session import get_async_db
from server.app.models.auth import User
from server.app.schemas.auth import UserLoginPayload
from sqlalchemy.ext.asyncio import AsyncSession
from server.app.services.db import get_create_update_delete
from server.app.config.config import variables
from server.app.services.jwt import create_access_token, create_refresh_token


router = APIRouter()

@router.get('/login',status_code=200)
async def login(response:Response, db:AsyncSession=Depends(get_async_db)):
    try:
        # user= await get_create_update_delete.get_one(
        #     db=db,
        #     model=User,
        #     filters={
        #         "email":data.email
        #     }
        # )
        # if not user:
        #     raise HTTPException(
        #         status_code=status.HTTP_404_NOT_FOUND,
        #         detail="User not found"
        #     )

        access_token=await create_access_token(
            data={
                "user_id":"rkayjim@gmail.com"
            }
        )
        refresh_token=await create_refresh_token(
            data={
                "user_id":"rkayjim@gmail.com"
            }
        )
        response.set_cookie(
            key="at_allow_me",
            value=access_token["access_token"],
            httponly=True,      
            secure=True,        
            samesite= "none",     
            expires= access_token["expires_at"],        
            path = "/",
            domain= variables.auth_cookie_domain
        )

        response.set_cookie(
            key="rt_allow_me",
            value=refresh_token["refresh_token"],
            httponly=True,      
            secure=True,        
            samesite= "none",     
            max_age=refresh_token["expires_at"],        
            path = "/",
            domain= variables.auth_cookie_domain
        )
        return
    except HTTPException as e:
        print(e)
        raise e
    
    except ValueError as ve:
        print(ve)
        raise HTTPException(
            status_code=status.HTTP_406_NOT_ACCEPTABLE,
            detail=str(ve)
        )
    
    except Exception as e:
        print(e)
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Server Error Occurred"
        )
