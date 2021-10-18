from domain.interfaces import IUseCase
from domain.interfaces import ICreateFailureRequest, IFailureRepository, IUserRepository
from domain.responses import SuccessResponse, FailResponse


class CreateFailureUseCase(IUseCase):

    def __init__(self, failure_repository: IFailureRepository, user_repository: IUserRepository):
        self._failure_repository = failure_repository
        self._user_repository = user_repository

    def execute(self, request: ICreateFailureRequest) -> SuccessResponse | FailResponse:
        user = request.user
        failure = request.failure

        user.create_failure(failure)
        self._failure_repository.add(failure)
        self._user_repository.update(user)

        return SuccessResponse()
