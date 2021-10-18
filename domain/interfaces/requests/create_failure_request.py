from domain.interfaces import IRequest
from domain.entities import User, Failure
from abc import abstractmethod


class ICreateFailureRequest(IRequest):

    @property
    @abstractmethod
    def user(self) -> User:
        pass

    @property
    @abstractmethod
    def failure(self) -> Failure:
        pass
