from abc import abstractmethod
from domain.interfaces.base import IRequest, IResponse


class IUseCase:

    @abstractmethod
    def execute(self, request: IRequest) -> IResponse:
        pass
