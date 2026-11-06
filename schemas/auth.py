from pydantic import BaseModel

class LoginDate(BaseModel):
    email: str
    password: str