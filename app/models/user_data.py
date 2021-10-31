class UserData:
    """User data.

    Represents the basic information of a user.
    """

    def __init__(self, username: str, password: str) -> None:
        """Initializes the user data.

        Args:
            username (str): The username of the user.
            password (str): The password of the user.
        """

        self.username = username
        self.password = password
