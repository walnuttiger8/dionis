from abc import abstractmethod, ABCMeta

from domain import ISpecification
from domain.entities import UserInfo


class IUserInfoRepository(metaclass=ABCMeta):

    def add(self, user_info: UserInfo) -> None:
        pass

    @abstractmethod
    def get(self, user_info_id: int) -> UserInfo:
        pass

    @abstractmethod
    def get_from_user_id(self, user_id: int) -> UserInfo:
        pass

    @abstractmethod
    def all(self) -> list[UserInfo]:
        pass

    @abstractmethod
    def remove(self, user_info_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, specifications: list[ISpecification]) -> list[UserInfo]:
        pass

    @abstractmethod
    def update(self, user_info: UserInfo) -> None:
        pass
