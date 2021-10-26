from domain import IResponse, IUserInfoRepository, UserInfoResponse, FailResponse
from domain.interfaces import IUseCase
from domain.requests import GetUserInfoRequest


class GetUserInfoUseCase(IUseCase):

    def __int__(self, user_info_repository: IUserInfoRepository):
        self._user_info_repository = user_info_repository

    def execute(self, request: GetUserInfoRequest) -> UserInfoResponse | FailResponse:
        user = request.user
        info = self._user_info_repository.get_from_user_id(user.id)

        if info:
            return UserInfoResponse(info)
        return FailResponse()
