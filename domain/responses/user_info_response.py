from domain import SuccessResponse, UserInfo


class UserInfoResponse(SuccessResponse):

    def __init__(self, user_info: UserInfo):
        self._user_info = user_info

    @property
    def user_info(self) -> UserInfo:
        return self._user_info
