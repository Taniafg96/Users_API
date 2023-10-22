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
    
class UpdateUserModel(BaseModel):
    id: int   
    email: str | None = None
    password: str | None = None
    is_active: bool | None = None
    is_superuser: bool | None = None
    updated_at: str | None = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    @validator("email", pre=True)
    def email_format(cls, email):  
        if is_valid_email(email):
            return email
        raise ValueError("Invalid email format")
    
    @validator("password", pre=True, always=True)    
    def email_format(cls, password):  
        if is_valid_password(password):
            return password
        raise ValueError("Invalid password format")
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
    
    @validator("password", pre=True, always=True)    
    def email_format(cls, password):  
        if is_valid_password(password):
            return password
        raise ValueError("Invalid password format")

def is_valid_email(email):
    regex = re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
    is_valid = bool(re.fullmatch(regex, email))
    if is_valid:
        return True
    return False

def is_valid_password(password):
    # Regex -> Minimum eight characters, at least one letter and one number
    regex = re.compile(r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$")
    is_valid = bool(re.fullmatch(regex, password))
    if is_valid:
        return True
    return False