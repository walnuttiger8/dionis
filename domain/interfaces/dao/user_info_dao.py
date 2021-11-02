from abc import ABC, abstractmethod

from domain.entities import UserInfo
from domain.interfaces.dao.base import IDao


class IUserInfoDao(IDao[UserInfo], ABC):

    @abstractmethod
    def from_user_id(self, user_id: int) -> UserInfo | None:
        pass
