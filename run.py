from passwords import User
from credentials import Credentials

def create_user(first_name,last_name,password):
    """
    Function that facilitates the cretion of new users
    """
    new_user = User(first_name,last_name,password)
    return new_user

def save_user(user):
    """
    Function that saves a new user`s account
    """
    user.save_user()

def log_in(first_name,last_name,password):
    """
    Function that enables the user to log into his account
    """
    log_in == User.log_in(first_name,last_name,password)
    if log_in != False:
        return User.log_in(first_name,last_name,password)

def create_credentials(password,credentials_name,credentials_password):
    """
    Fuction that allows useres to create their own credentials
    """
    new_credentials = Credentials(password,credentials_name,credentials_password)
    return new_credentials

def save_credentials(credentials):
    """
    Function that allows users to save their credentials
    """
    credentials.save_credentials()

def check_existing_credentials(credentials_name):
    """
    Function that allows users to find their existing credentials
    """
    return Credentials.credentials_exist(credentials_name)

def display_credentials(credentials_password):
    """
    Function that lists all the saved credentials
    """
    return Credentials.display_credentials(credentials_password)
