from user import User


class UserRepository:

    def __init__(self) -> None:
        self.__users_list = []

    def __init__(self, users_list: list[User]) -> None:
        self.__users_list = users_list

    def add_user(self, user_for_add: User) -> None:
        self.__users_list.append(user_for_add)
    
    def logout_user(self, user_for_del: User) -> User:
        if user_for_del in self.__users_list:
            return self.__users_list.pop(self.__users_list.index(user_for_del))
        return None
    
    def find_user_by_name(self, username: str) -> User:
        for user in self.__users_list:
            if user.name == username:
                return user
        return None

    def logout_all_users(self) -> list[User]:
        admins_list = []
        for user in self.__users_list:
            if user.is_admin:
                admins_list.append(user)
        self.__users_list = admins_list
        return self
    
    @property
    def users_list(self) -> list[User]:
        return self.__users_list
    
    @users_list.setter
    def users_list(self, users_list: list[User]) -> None:
        self.__users_list = users_list
    
    def __str__(self) -> str:
        return f'{self.__users_list}'

    
if __name__ == "__main__":
    user1 = User('Alex19', 'a927dc21ec21134f6fbfbdfff4cec5d3b')
    user2 = User('Marta08', 'cf41e576a8a1cbc5893eefe02f37eedd9')
    repo = UserRepository([user1, user2])

    
    admin = User('admin', '0e789ec2cfcc190d040f5182b118add0d')
    admin.is_admin= True
    repo.add_user(admin)


    repo.logout_all_users()
    for user in repo.users_list:
        print(user)
    
