import unittest
from credentials import Credentials

class TestCredentials(unittest.TestCase):
    """
    Class that puts all the behaviours of the credentials to the test
    """
    def setUp(self):
        """
        Function that creates new credentials before each test
        """
        self.new_credentials = Credentials('RAJIV12345','instagram','KINYA12345')

    def test__init__(self):
        """
        Test that checks if formulation of new credential instances is correctly done
        """    





if __name__ == "__main__":
    unittest.main()