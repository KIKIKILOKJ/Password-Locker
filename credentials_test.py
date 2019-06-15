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

    def tearDown(self):
        """
        Method destroys results of previous tests to provide room for new tests
        """
        Credentials.credentials_list = []

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

    def test_save_multiple_credentials(self):
        """
        Tests whether various users credentials are being saved
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('RAJIV12345','instagram','KINYA12345')
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list),2)


    def test_generate_password(self):
        """
        Tests if a password can be generated
        """
        generated_password = self.new_credentials.generate_password()
        self.assertEqual(len(generated_password),8)

    def test_display_credentials(self):
        """
        Tests if once user has logged in then the credentials saved are listed.
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('RAJIV12345','instagram','KINYA12345')
        test_credentials.save_credentials
        self.assertEqual(len(Credentials.display_credentials('RAJIV12345')),1)

    def test_credentials_exist(self):
        """
        Test to see if a user`s existing credentials can be found if they exist
        """
        self.new_credentials.save_credentials()
        test_credentials = Credentials('RAJIV12345','instagram','KINYA12345')
        test_credentials.save_credentials()
        credentials_exist = Credentials.credentials_exist('instagram')
        self.assertTrue(credentials_exist)

if __name__ == "__main__":
    unittest.main()