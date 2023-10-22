from fastapi import APIRouter, Request, status
from fastapi.responses import JSONResponse
from src.adapters.users import UsersAdapter

from src.models.user_model import CreateUserModel, UpdateUserModel


router = APIRouter()

@router.get("/",
            description="Get current user",
            response_description="Current user existing in database",)
def get_current_user(request: Request):
    usersAdapter = UsersAdapter()
    
    if (user := usersAdapter.read_one_user(id)) is not None:
        return user
    return JSONResponse(
        content={"detail": f"Error getting user {id} in database"},
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.get("/all",
            description="Get all users",
            response_description="List of each users existing in database",)
def get_all_users(request: Request):
    usersAdapter = UsersAdapter()
    if (users := usersAdapter.read_users()) is not None:
        return users
    return JSONResponse(
        content={"detail": f"Error getting users from database"},
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.get("/{user_id}",
             description="Get user by id",
             response_description="User existing in database",)
def get_user_by_id(request: Request, user_id: int):
    usersAdapter = UsersAdapter()
    
    if (user := usersAdapter.read_one_user(user_id)) is not None:
        return user
    return JSONResponse(
        content={"detail": f"Error getting user {user_id} in database"},
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.post("/create",
             description="Create user",
             response_description="User existing in database",)
def create_user(request: Request, user: CreateUserModel):
    usersAdapter = UsersAdapter()
    if usersAdapter.create_user(user):
        return JSONResponse(
            content={"detail": f"New User created"},
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content={"detail": f"Error created user"},
        status_code=status.HTTP_404_NOT_FOUND
    )
        
@router.put("/",
            description="Update user by id",
            response_description="User existing in database",)
def put_user_by_id(request: Request, user: UpdateUserModel):
    usersAdapter = UsersAdapter()
    if usersAdapter.update_user(user):
        return JSONResponse(
            content={"detail": f"New User updated"},
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content={"detail": f"Error updated user"},
        status_code=status.HTTP_404_NOT_FOUND
    )

@router.delete("/{user_id}",
               description="Delete user by id",
               response_description="User existing in database",)
def delete_user_by_id(request: Request, user_id: int):
    usersAdapter = UsersAdapter()
    if usersAdapter.delete_user(user_id):
        return JSONResponse(
            content={"detail": f"New User deleted"},
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content={"detail": f"Error deleted user"},
        status_code=status.HTTP_404_NOT_FOUND
    )