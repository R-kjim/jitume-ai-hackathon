from pydantic import BaseModel, EmailStr


class UserLoginPayload(BaseModel):
    email: EmailStr
    password: str

class UserLoginResponse( BaseModel ):
    first_name: str
    last_name: str
    