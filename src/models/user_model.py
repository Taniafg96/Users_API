from datetime import datetime
import re
from pydantic import BaseModel, validator

class UsersModel(BaseModel):
    id: int
    name: str
    email: str
    is_active: bool
    is_superuser: bool
    created_at: datetime
    updated_at: datetime
    
class CreateUserModel(BaseModel):
    name: str
    email: str
    password: str
    is_active: bool | None = True
    is_superuser: bool | None = False
    created_at: str | None = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    updated_at: str | None = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @validator("email", pre=True, always=True)
    def email_format(cls, email):  
        if is_valid_email(email):
            return email
        raise ValueError("Invalid email format")

def is_valid_email(email):
    regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    is_valid = bool(re.fullmatch(regex, email))
    if is_valid:
        return True
    return False