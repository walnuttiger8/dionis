from domain import IUseCase, IResponse, IUserAccountRepository, AuthorizationRequest, FailResponse, \
    IUserRepository, AuthorizationResponse


class AuthorizationUseCase(IUseCase):

    def __init__(self, user_account_repository: IUserAccountRepository, user_repository: IUserRepository):
        self._user_account_repository = user_account_repository
        self._user_repository = user_repository

    def execute(self, request: AuthorizationRequest) -> IResponse:
        login = request.login
        password_hash = request.password_hash

        account = self._user_account_repository.get_from_login(login)
        if not account:
            return FailResponse()

        if account.password_hash != password_hash:
            return FailResponse()

        user = self._user_repository.get(account.user_id)
        if not user:
            return FailResponse()

        return AuthorizationResponse(user)
