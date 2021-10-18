from domain.entities.user import User
from domain.interfaces.base.specification import ISpecification
from abc import abstractmethod


class IUserRepository:

    @abstractmethod
    def add(self, user: User) -> None:
        pass

    @abstractmethod
    def get(self, user_id: int) -> User:
        pass

    @abstractmethod
    def all(self) -> list[User]:
        pass

    @abstractmethod
    def remove(self, user_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, specification: list[ISpecification]) -> list[User]:
        pass

    @abstractmethod
    def update(self, user: User) -> None:
        pass
