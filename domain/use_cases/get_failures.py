from domain.interfaces import IUseCase, IFailureRepository, IGetFailuresRequest
from domain.responses import GetFailuresResponse, FailResponse


class GetFailuresUseCase(IUseCase):

    def __init__(self, failure_repository: IFailureRepository):
        self._failure_repository = failure_repository

    def execute(self, request: IGetFailuresRequest) -> GetFailuresResponse | FailResponse:
        specifications = request.specifications
        if specifications:
            failures = self._failure_repository.filter(specifications)
        else:
            failures = self._failure_repository.all()

        return GetFailuresResponse(failures)
