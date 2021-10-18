from domain.entities.failure import Failure
from domain.interfaces.base.specification import ISpecification
from abc import abstractmethod


class IFailureRepository:

    @abstractmethod
    def add(self, failure: Failure) -> None:
        pass

    @abstractmethod
    def get(self, failure_id: int) -> Failure:
        pass

    @abstractmethod
    def all(self) -> list[Failure]:
        pass

    @abstractmethod
    def remove(self, failure_id: int) -> None:
        pass

    @abstractmethod
    def filter(self, specifications: list[ISpecification]) -> list[Failure]:
        pass

    @abstractmethod
    def update(self, failure: Failure) -> None:
        pass
