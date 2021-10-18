from domain.responses import SuccessResponse, FailResponse
from domain.interfaces import IUseCase, IFailureRepository, IUpdateFailureRequest


class UpdateFailureUseCase(IUseCase):
    def __init__(self, failure_repository: IFailureRepository):
        self._failure_repository = failure_repository

    def execute(self, request: IUpdateFailureRequest) -> SuccessResponse | FailResponse:
        user = request.user
        failure = request.failure

        if failure.creator != user:
            return FailResponse()

        self._failure_repository.update(failure)
        return SuccessResponse()
