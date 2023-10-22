from src.auth.hash_password import HashPassword
from src.models.user_model import UpdateUserModel


class UsersDTO:
    
    def update_query(self, user: UpdateUserModel) -> str | None:
        params = []

        if user.email is not None:
            params.append(f"email = '{user.email}'")
        if user.password is not None:
            password_hash = HashPassword().create_hash(user.password) 
            params.append(f"password = '{password_hash}'")
        if user.is_active is not None:
            params.append(f"is_active = {user.is_active}")
        if user.is_superuser is not None:
            params.append(f"is_superuser = {user.is_superuser}")
            
        if bool(params):
            params.append(f"updated_at = '{user.updated_at}'")
            return ', '.join(params)
        return None