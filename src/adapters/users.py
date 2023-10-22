from src.adapters.users_dto import UsersDTO
from src.auth.hash_password import HashPassword
from src.conector.mariadb import MariaDBConector
from src.logger import Logger
from src.models.user_model import CreateUserModel, UpdateUserModel, UsersModel
from src.static.users_queries import CREATE_USER, DELETE_USER, READ_ONE_USER, READ_USERS, UPDATE_USER


class UsersAdapter:
    logger = Logger(__file__)
    
    def read_users(self) -> list[UsersModel] | None:
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
            self.logger.info('Users have been successfully obtained')
            return users_list
        self.logger.error("There have been problems obtaining users")
        return None
    
    def read_one_user(self, id: int) -> UsersModel | None:
        mariaDBConector = MariaDBConector()
        if (user := mariaDBConector.read_table(READ_ONE_USER.format(id))) is not None:
            self.logger.info(f'User {id} has been successfully obtained')
            return UsersModel(
                    id=user[0][0],
                    name=user[0][1],
                    email=user[0][2],
                    is_active=user[0][4],
                    is_superuser=user[0][5],
                    created_at=user[0][6],
                    updated_at=user[0][7],
                )
        self.logger.error(f"There has been a problem obtaining user {id}")
        return None
    
    def create_user(self, user: CreateUserModel):
        mariaDBConector = MariaDBConector()
        password_hash = HashPassword().create_hash(user.password)
        
        create_user_query = CREATE_USER.format(
                                user.name,
                                user.email,
                                password_hash,
                                user.is_active,
                                user.is_superuser,
                                user.created_at,
                                user.updated_at)
        if mariaDBConector.modify_table(create_user_query):
            self.logger.info(f'User {user.name} has been successfully created')
            return True
        self.logger.error(f"There has been a problem creating user {user.name}")
        return False
    
    def update_user(self, user: UpdateUserModel):
        if (params := UsersDTO().update_query(user)) is not None:
            print(params)
            mariaDBConector = MariaDBConector()
            update_user_query = UPDATE_USER.format(
                                    params,
                                    user.id)
            print(update_user_query)
            if mariaDBConector.modify_table(update_user_query):
                self.logger.info(f'User {id} has been successfully updated')
                return True
        self.logger.error(f"There has been a problem updating user {id}")
        return False
    
    def delete_user(self, id: int):
        mariaDBConector = MariaDBConector()
        delete_user_query = DELETE_USER.format(id)
        if mariaDBConector.modify_table(delete_user_query):
            self.logger.info(f'User {id} has been successfully deleted')
            return True
        self.logger.error(f"There has been a problem deleting user {id}")
        return False
    