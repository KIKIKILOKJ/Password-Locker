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

    