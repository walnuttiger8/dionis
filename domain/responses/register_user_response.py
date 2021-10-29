from domain.responses import SuccessResponse
from domain.entities import User


class RegisterUserResponse(SuccessResponse):

    def __init__(self, user: User):
        self._user = user

    @property
    def user(self) -> User:
        return self._user
