from abc import abstractmethod, ABC
from typing import TypeVar, Generic

T = TypeVar("T")


class IDao(ABC, Generic[T]):

    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def read(self, entity_id: int) -> T | None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    @abstractmethod
    def delete(self, entity_id: int) -> None:
        pass
