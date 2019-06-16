from credentials import Credentials
class User:
    """
    Class that genrates new users in form of a list
    """
    user_list = []

    def __init__(self,first_name,last_name,password):
        """
        Method defines the properties to be contained in each object
        
        Args:
            first_name: New user first name.
            last_name: New user last name.
            password: New user password.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def save_user(self):
        """
        This method allows for new user to saved in a list
        """
        User.user_list.append(self)
    
    @classmethod
    def user_exist(cls,first_name):
        """
        Function that allows finding of an existing user
        """
        for user in cls.user_list:
            if user.first_name == first_name:
                return True
        return False

    @classmethod
    def display_user(cls):
        """
        Method that shows a list of users saved
        """
        return cls.user_list

    @classmethod
    def log_in(cls,first_name,last_name,password):
        """
        Method that enables users to access their credentials
        """
        for user in cls.user_list:
            if user.first_name == first_name and user.last_name == last_name and user.password == password:
                return Credentials.credentials_list
        return False