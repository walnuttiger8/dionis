from abc import abstractmethod

from domain import Failure, User
from domain.interfaces import IRequest


class DeleteFailureRequest(IRequest):

    @property
    @abstractmethod
    def failure(self) -> Failure:
        pass

    @property
    @abstractmethod
    def user(self) -> User:
        pass
