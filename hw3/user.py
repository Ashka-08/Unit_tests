class User:
    
    def __init__(self, name: str, password: str):
        self.__name = name
        self.__password = password
        self.__is_admin = False
    
    # def add_admin_access(self) -> None:
    #     self.__is_admin = True

    @property
    def name(self) -> str:
        return self.__name
    
    @name.setter
    def name(self, name: str) -> None:
        self.__name = name
    
    @property
    def password(self) -> str:
        return self.__password
    
    @password.setter
    def password(self, password: str) -> None:
        self.__password = password
    
    @property
    def is_admin(self) -> bool:
        return self.__is_admin
    
    @is_admin.setter
    def is_admin(self, is_admin: bool) -> None:
        self.__is_admin = is_admin
    
    def __repr__(self) -> str:
        return f'User {self.__name}, is_admin: {self.__is_admin}'

    def __eq__(self, other):
        if isinstance(other, User):
            return self.__name == other.__name
        return NotImplemented


if __name__ == "__main__":
    user1 = User('Alex19', 
            'a927dc21ec21134f6fbfbdfff4cec5d3bfef91104503339b2a9adb0190e48ebf')
    print(user1)