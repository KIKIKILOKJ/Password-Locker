import unittest
from passwords import User
from credentials import Credentials

class TestUser(unittest.TestCase):
    """
    Class that definres all tests for various behaviours of the application
    """
    def setUp(self):
        """
        function that creates a new account before each test
        """
        self.new_user = User('Peter','Max','RAJIV12345')

    def test__init__(self):
        """
        Test that checks if formulation of new user instances is correctly done
        """
        self.assertEqual(self.new_user.first_name,'Peter')
        self.assertEqual(self.new_user.last_name,'Max')
        self.assertEqual(self.new_user.password,'RAJIV12345')

    def test_save_user(self):
        """
        Test to check if user description has been added onto the list
        """
        self.new_user.save_user()
        self.assertEqual(len(User.user_list),3)

    def test_user_exist(self):
        """
        Test to figure out if a user exists
        """
        self.new_user.save_user()
        test_user = User('Peter','Max','RAJIV12345')
        test_user.save_user()
        user_exists = User.user_exist('Peter')
        self.assertTrue(user_exists)
    
    def test_display_user(self):
        """
        Tests if a list of users saved cn be shown
        """
        self.assertEqual(User.display_user(),User.user_list)

    def test_log_in(self):
        """
        Test if a user can log in to their account
        """
        self.new_user.save_user()
        test_user = User('Peter','Max','RAJIV12345')
        test_user.save_user()
        found_credentials = User.log_in('Peter','Max','RAJIV12345')
        self.assertEqual(found_credentials, Credentials.credentials_list)


if __name__ == "__main__":
    
    unittest.main()