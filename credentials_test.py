import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class that puts all the behaviours of the credentials to the test
    """
    def test_check_user(self):
        """
        The function checks if the log in function is fully operational
        """
        self.new_user = User('Peter','Max','RAJIV12345')
        self.new_user.save_user()
        user2 = User('John','Max','RAJIV12345')
        user2.save_user

        for user in User.user_list:
            if user.first_name == user2.first_name and user.password == user2.password:
                current_user == user.first_name
        return current_user

        self.assertEqual(current_user,credentials.check_user(user2.password,user2.first_name))

if __name__ == "__main__":
    unittest.main()