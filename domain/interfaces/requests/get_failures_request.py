from abc import abstractmethod
from domain.interfaces import IRequest, ISpecification


class IGetFailuresRequest(IRequest):

    @property
    @abstractmethod
    def specifications(self) -> list[ISpecification]:
        pass
