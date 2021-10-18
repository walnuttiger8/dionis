from domain.interfaces import ICreateFailureRequest
from domain.entities import User, Failure


class CreateFailureRequest(ICreateFailureRequest):

    def __init__(self, user: User, failure: Failure):
        self._user = user
        self._failure = failure

    @property
    def user(self) -> User:
        return self._user

    @property
    def failure(self) -> Failure:
        return self._failure
