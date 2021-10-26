from domain import IRequest, UserAccount, UserInfo


class RegisterUserRequest(IRequest):

    def __init__(self, user_account, user_info):
        self._user_account = user_account
        self._user_info = user_info

    @property
    def user_account(self) -> UserAccount:
        return self._user_account

    @property
    def user_info(self) -> UserInfo:
        return self._user_info
