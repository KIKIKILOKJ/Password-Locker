import unittest
from passwords import User

class TestUser(unittest.TestCase):
    """
    Class that definres all tests for various behaviours of the application
    """
    def setUp(self):
        """
        function that a new account before each test
        """
        self.new_user = User('Peter','Max','RAJIV12345')

    def test__init__(self):
        """
        Test that checks if formulation of new user instances is correctly done
        """
        self.assertEqual(self.new_user.first_name,'Peter')
        self.assertEqual(self.new_user.last_name,'Max')
        self.assertEqual(self.new_user.password,'RAJIV12345')


if __name__ == "__main__":
    
    unittest.main()