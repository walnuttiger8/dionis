from domain import IUseCase, RegisterUserRequest, RegisterUserResponse, IUserInfoRepository, \
    IUserAccountRepository, UserAccount, FailResponse, User, IUserRepository


class RegisterUserUseCase(IUseCase):
    def __init__(self, user_info_repository: IUserInfoRepository, user_account_repository: IUserAccountRepository,
                 user_repository: IUserRepository):
        self._user_info_repository = user_info_repository
        self._user_account_repository = user_account_repository
        self._user_repository = user_repository

    def _validate_account(self, account: UserAccount) -> str:
        if self._user_account_repository.get_from_login(account.login):
            return "account with such login already exists"
        return ""

    def _create_user(self) -> User:
        user = User()
        return self._user_repository.add(user)

    def execute(self, request: RegisterUserRequest) -> RegisterUserResponse | FailResponse:
        account = request.user_account
        info = request.user_info

        validation_msg = self._validate_account(account)
        if validation_msg:
            print(validation_msg)
            return FailResponse()

        user = self._create_user()
        account.user_id = user.id
        info.user_id = user.id

        self._user_account_repository.add(account)
        self._user_info_repository.add(info)
        return RegisterUserResponse(user)
