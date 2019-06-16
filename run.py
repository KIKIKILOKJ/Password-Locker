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