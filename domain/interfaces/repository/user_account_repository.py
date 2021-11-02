from abc import abstractmethod, ABC
from domain.interfaces.repository.base import IRepository
from domain.entities import UserAccount


class IUserAccountRepository(IRepository[UserAccount], ABC):

    @abstractmethod
    def get_from_user_id(self, user_id: int) -> UserAccount:
        pass

    @abstractmethod
    def get_from_login(self, login: str) -> UserAccount:
        pass
