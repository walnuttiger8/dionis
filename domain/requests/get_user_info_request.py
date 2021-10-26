from domain.entities import User
from domain.interfaces import IRequest
from abc import abstractmethod


class GetUserInfoRequest(IRequest):

    @property
    @abstractmethod
    def user(self) -> User:
        pass
