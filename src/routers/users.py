from fastapi import APIRouter, Request
from src.adapters.users import UsersAdapter

from src.models.user_model import CreateUserModel


router = APIRouter()

@router.get("/",
            description="Get current user",
            response_description="Current user existing in database",)
def get_current_user(request: Request):
    return {"users": "users"}

@router.get("/all",
            description="Get all users",
            response_description="List of each users existing in database",)
def get_all_users(request: Request):
    usersAdapter = UsersAdapter()
    users = usersAdapter.read_users()
    return users

@router.get("/{user_id}",
             description="Get user by id",
             response_description="User existing in database",)
def get_user_by_id(request: Request, user_id: int):
    return {"users": "users"}

@router.post("/create",
             description="Create user",
             response_description="User existing in database",)
def create_user(request: Request, user: CreateUserModel):
    usersAdapter = UsersAdapter()
    usersAdapter.create_user(user)
    return {"users": "users"}

@router.put("/{user_id}",
            description="Update user by id",
            response_description="User existing in database",)
def put_user_by_id(request: Request, user_id: int, user: CreateUserModel):    
    return user

@router.delete("/{user_id}",
               description="Delete user by id",
               response_description="User existing in database",)
def delete_user_by_id(request: Request, user_id: int):
    return {"users": user_id}