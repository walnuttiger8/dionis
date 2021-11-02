from domain.interfaces.base.specification import ISpecification
from abc import abstractmethod, ABC
from typing import Generic, TypeVar

T = TypeVar("T")


class IRepository(ABC, Generic[T]):

    @abstractmethod
    def add(self, entity: T) -> None:
        pass

    @abstractmethod
    def get(self, entity_id: int) -> T:
        pass

    @abstractmethod
    def all(self) -> list[T]:
        pass

    @abstractmethod
    def remove(self, entity_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, specifications: list[ISpecification]) -> list[T]:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass
