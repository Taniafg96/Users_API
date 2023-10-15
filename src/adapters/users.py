from src.conector.mariadb import MariaDBConector
from src.models.user_model import CreateUserModel, UsersModel
from src.static.users_queries import CREATE_USER, DELETE_USER, READ_ONE_USER, READ_USERS, UPDATE_USER


class UsersAdapter:
    def read_users(self):
        mariaDBConector = MariaDBConector()
        if (users := mariaDBConector.read_table(READ_USERS)) is not None:
            users_list = []
            for user in users:
                users_list.append(UsersModel(
                    id=user[0],
                    name=user[1],
                    email=user[2],
                    is_active=user[4],
                    is_superuser=user[5],
                    created_at=user[6],
                    updated_at=user[7],
                ))
            return users_list
        raise Exception("Error reading users")
    
    def read_one_user(self, id: int):
        mariaDBConector = MariaDBConector()
        if (user := mariaDBConector.read_table(READ_ONE_USER.format(id))) is not None:
            return user
        raise Exception("Error reading user")
    
    def create_user(self, user: CreateUserModel):
        mariaDBConector = MariaDBConector()
        create_user_query = CREATE_USER.format(
                                user.name,
                                user.email,
                                user.password,
                                user.is_active,
                                user.is_superuser,
                                user.created_at,
                                user.updated_at)
        if mariaDBConector.modify_table(create_user_query):
            return True
        return False
    
    def update_user(self, user: CreateUserModel, id: int):
        mariaDBConector = MariaDBConector()
        update_user_query = UPDATE_USER.format(
                                user.name,
                                user.email,
                                user.password,
                                id)
        if mariaDBConector.modify_table(update_user_query):
            return True
        return False
    
    def delete_user(self, id: int):
        mariaDBConector = MariaDBConector()
        delete_user_query = DELETE_USER.format(id)
        if mariaDBConector.modify_table(delete_user_query):
            return True
        return False
    