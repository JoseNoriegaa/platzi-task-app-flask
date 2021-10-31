from typing import Optional

# Flask Login
from flask_login import UserMixin  # type: ignore

# Firestore service
from app.firestore_service import get_user

# Models
from .user_data import UserData


class UserModel(UserMixin):
    """User model."""

    def __init__(self, user_data: UserData) -> None:
        """
        Args:
            user_data (UserData): User data
        """

        self.id = user_data.username
        self.password = user_data.password

    def get_id(self) -> str:
        """Gets the user id.

        Returns:
            str: The user id.
        """

        return self.id


    @staticmethod
    def from_document(document) -> Optional['UserModel']:
        """Creates a user model from a document.

        Args:
            document: The firestore user document.

        Returns:
            UserModel: The user model.
        """

        doc_to_dict = document.to_dict()

        if doc_to_dict is None:
            return None

        user_data = UserData(
            username=document.id,
            password=doc_to_dict['password']
        )

        return UserModel(user_data)

    @staticmethod
    def query(user_id: str) -> Optional['UserModel']:
        """Queries the user.

        Args:
            user_id (str): The id of the user.

        Returns:
            UserModel: The user model.
        """

        document = get_user(user_id)

        if document is None:
            return None

        return UserModel.from_document(document)
