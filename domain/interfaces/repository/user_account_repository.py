from abc import abstractmethod, ABCMeta

from domain.interfaces import ISpecification
from domain.entities import UserAccount


class IUserAccountRepository(metaclass=ABCMeta):

    def add(self, user_account: UserAccount) -> None:
        pass

    @abstractmethod
    def get(self, user_account_id: int) -> UserAccount:
        pass

    @abstractmethod
    def get_from_user_id(self, user_id: int) -> UserAccount:
        pass

    @abstractmethod
    def get_from_login(self, login: str) -> UserAccount:
        pass

    @abstractmethod
    def all(self) -> list[UserAccount]:
        pass

    @abstractmethod
    def remove(self, user_account_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, specifications: list[ISpecification]) -> list[UserAccount]:
        pass

    @abstractmethod
    def update(self, user_account: UserAccount) -> None:
        pass
