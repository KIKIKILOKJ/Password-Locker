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
        
        #elif short_code == 'dl':
         #   """
         #   dl = Display names of users saved
         #   """
         #   if display_user():
         #       print("\n")
          #      print("Here are the users of the application")
          #      print("-"*10)
          #      for user in user_list():
          #          print(f"{user.first_name}")
          #          print("-"*10)
          #  else:
           #     print("Password Locker has no available users.\n Be the first user:")
        
        elif short_code == 'li':
            """
            Users log in to their account
            """
            print("\n")
            print("Log into your Account")
            print("Enter the user name")
            first_name = input()

            print("Enter the password")
            password = input()

            if log_in(first_name,last_name,password) == None:
                print("\n")
                print("Please try again or create an account")
                print("\n")
            
            else:
                log_in(first_name,last_name,password)
                print("\n")
                print(f"{first_name} WELCOME TO YOUR CREDENTIALS\n Use the short codes")
                
                while True:
                    print("Short codes: ac-Add credentials, dc-Display credentials, cg-Create credentials with a generated password, ex-Exit credentials")
                    
                    short_code = input().lower()
                    if short_code == "ac":
                        """
                        Create Credentials
                        """
                        print("\n")
                        print("New Credentials")
                        print("-"*10)

                        print("Name of the credentials ....")
                        credentials_name = input()

                        print("Password of the credentials ....")
                        credentials_password = input()

                        save_credentials(create_credentials(password,credentials_name,credentials_password))

                        print(f"{credentials_name} have been created and saved")

                    elif short_code == 'dc':
                        '''
                        Displaying credential name and password
                        '''

                        if display_credentials(credentials_password):
                            print("\n")
                            print(f"{first_name}\'s credentials")
                            print("-"*10)

                            for credential in display_credentials(credentials_password):
                                print(f"Account ..... {credential.credential_name}")
                                print(f"Password .... {credential.credential_password}")
                                print("-"*10)

                        else:
                            print("\n")
                            print("You have no credentials")
                            print("\n")

                   