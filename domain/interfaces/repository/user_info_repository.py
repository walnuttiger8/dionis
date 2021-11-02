from abc import abstractmethod, ABC
from domain.interfaces.repository.base import IRepository

from domain.entities import UserInfo


class IUserInfoRepository(IRepository[UserInfo], ABC):

    @abstractmethod
    def get_from_user_id(self, user_id: int) -> UserInfo:
        pass
