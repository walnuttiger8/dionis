from abc import abstractmethod
from domain.entities.failure import Failure


class IFailureDao:

    @abstractmethod
    def create(self, failure: Failure) -> None:
        pass

    @abstractmethod
    def read(self, failure_id: int) -> Failure | None:
        pass

    @abstractmethod
    def update(self, failure: Failure) -> None:
        pass

    @abstractmethod
    def delete(self, failure_id) -> None:
        pass
