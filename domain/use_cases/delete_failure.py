from domain import IResponse, DeleteFailureRequest, IFailureRepository, SuccessResponse
from domain.interfaces import IUseCase


class DeleteFailureUseCase(IUseCase):

    def __init__(self, failure_repository: IFailureRepository):
        self._failure_repository = failure_repository

    def execute(self, request: DeleteFailureRequest) -> IResponse:
        user = request.user
        failure = request.failure

        user.delete_failure(failure)
        self._failure_repository.remove(failure.id)
        return SuccessResponse()
