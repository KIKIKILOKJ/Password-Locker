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
        self.assertEqual(self.new_credentials.password,'RAJIV12345')
        self.assertEqual(self.new_credentials.credentials_name,'instagram')
        self.assertEqual(self.new_credentials.credentials_password,'KINYA12345')

    def test_save_credentials(self):
        """
        Tests that the user`s credentials have been added to the credentials list
        """
        self.new_credentials.save_credentials()

    def test_generate_password(self):
        """
        Tests if a password can be generated
        """
        generated_password = self.new_credentials.generate_password()
        self.assertEqual(len(generated_password),8)


if __name__ == "__main__":
    unittest.main()