from configparser import ConfigParser
from contextlib import closing
from logging import Logger

import mariadb


class MariaDBConector:
    logger = Logger(__file__)
    
    def __init__(self) -> None:
        self.__config = ConfigParser()
        self.__config.read("config/mariadb.ini")
        
    def read_table(self, query: str):
        try:
            with closing(mariadb.connect(
                    user = self.__config["CREDENTIALS"]["user"],
                    password = self.__config["CREDENTIALS"]["password"],
                    host = self.__config["CREDENTIALS"]["host"],
                    port = int(self.__config["CREDENTIALS"]["port"]),
                    database = self.__config["CREDENTIALS"]["database"],
                )) as conector:
                with closing(conector.cursor()) as cursor:
                    print(query)
                    cursor.execute(query)
                    return cursor.fetchall()
        except mariadb.Error as error:
            self.logger.error(f"Error: {error}")
            return None
    
    def modify_table(self, query: str) -> bool:
        try:
            with closing(mariadb.connect(
                    user = self.__config["CREDENTIALS"]["user"],
                    password = self.__config["CREDENTIALS"]["password"],
                    host = self.__config["CREDENTIALS"]["host"],
                    port = int(self.__config["CREDENTIALS"]["port"]),
                    database = self.__config["CREDENTIALS"]["database"],
                )) as conector:
                with closing(conector.cursor()) as cursor:
                    cursor.execute(query)
                    conector.commit()
                    return True
        except mariadb.Error as error:
            self.logger.error(f"Error: {error}")
            return False