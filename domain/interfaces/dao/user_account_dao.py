from abc import ABC, abstractmethod

from domain.entities import UserAccount
from domain.interfaces.dao.base import IDao


class IUserAccountDao(IDao[UserAccount], ABC):

    @abstractmethod
    def from_login(self, login: str) -> UserAccount | None:
        pass

    @abstractmethod
    def from_user_id(self, user_id: int) -> UserAccount | None:
        pass
