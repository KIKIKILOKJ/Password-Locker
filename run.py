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

def create_generated_password(credentials_name):
    """
    Function that generates a suitable password for the user
    """
    credentials_password = Credentials.generate_password()
    return credentials_password

def main():
    """
    Function that allows the app to run and be operated from the terminal
    """
    print("HEY!! WELCOME TO YOUR SECURE PASSWORD LOCKER APP \n Use these short codes to achieve you iontentions with the app")
    while True:
        print("Short codes:ca-Create account, dl-Display names of users, li-Log into your account, ex-Exist account")
        short_code = input().lower()
        if short_code == "ca":
            """
            ca = Create new account
            """
            print("\n")
            print("New Account")
            print("-"*10)

            print("First name ....")
            first_name = input()

            print("Last name ....")
            last_name = input()

            print("Password ....")
            password = input()

            save_user(create_user(first_name,last_name,password))

            print("\n")
            print(f"{first_name,last_name}WELCOME TO THE PASSWORD LOCKER")
            print("\n")