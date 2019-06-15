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


    
