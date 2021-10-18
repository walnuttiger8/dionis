from abc import abstractmethod
from domain.interfaces.base import IRequest
from domain.entities import User, Failure


class IUpdateFailureRequest(IRequest):

    @property
    @abstractmethod
    def user(self) -> User:
        pass

    @property
    @abstractmethod
    def failure(self) -> Failure:
        pass
