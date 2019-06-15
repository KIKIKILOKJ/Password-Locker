from random import choice
import string
class Credentials:
    """
    Class to create additional account information
    """

    credentials_list = []

    def __init__(self,password,credentials_name,credentials_password):
        """
        __init__ method defines the properties of credentials object
        
        Args:
            password: Password of the user logged in.
            credentials_name: Name of the account. 
            credentials_password: Password for the account.
        """
        self.password = password
        self.credentials_name = credentials_name
        self.credentials_password = credentials_password

    def save_credentials(self):
        """
        The method adds user`s credentials to the credentials list.
        """
        Credentials.credentials_list.append(self)

    def delete_credentials(self):
        """
        The method deletes a saved credentials from the credentials_list
        """

        Credentials.credentials_list.remove(self)


    @classmethod
    def generate_password(cls):
        """
        Function that allows the application to generate a password for the user
        """
        size = 8#password should be 8 characters long
        alphanum = string.ascii_uppercase + string.digits + string.ascii_lowercase#generate random alphabets and numbers
        password = ''.join(choice(alphanum)for num in range(size))
        return password

    @classmethod
    def display_credentials(cls,password):
        """
        Method that shows the saved credentials
        """
        user_credentials_list = []

        for credentials in cls.credentials_list:
            if credentials.password == password:
                user_credentials_list.append(credentials)
        return user_credentials_list

    @classmethod
    def credentials_exist(cls,name):
        """
        Method that checks if specific credentials exist
        
        Returns:
            Boolean: True or False based on whether the credentials exist
        """
        for credentials in cls.credentials_list:
            if credentials.credentials_name == name:
                return True
        return False

    
