from user_repository import UserRepository
from user import User
import unittest


class UsersRepoTest(unittest.TestCase):

    def test_logout_not_admins(self):
        user1 = User('Alex19', 'a927dc21ec21134f6fbfbdfff4cec5d3b')
        user2 = User('Marta08', 'cf41e576a8a1cbc5893eefe02f37eedd9')
        admin = User('admin', '0e789ec2cfcc190d040f5182b118add0d')
        admin.is_admin= True
        repo = UserRepository([user1, user2, admin])
        repo.logout_all_users()
        ideal = UserRepository([admin])
        self.assertEqual(repo.users_list, ideal.users_list)

# python -m unittest users_unittest.py -v
# coverage run -m unittest users_unittest.py
# coverage report
