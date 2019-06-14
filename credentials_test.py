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

if __name__ == "__main__":
    unittest.main()