from passlib.context import CryptContext

class HashPassword:
    __scheme = "bcrypt"
    __deprecated = "auto"
    
    def __init__(self):
        self.__pwd_context = CryptContext(
                                schemes=[self.__scheme], 
                                deprecated=self.__deprecated
                            )
    
    def create_hash(self, password):
        return self.__pwd_context.hash(password)
    
    def verify_hash(self, password, password_hash):
        return self.__pwd_context.verify(password, password_hash)