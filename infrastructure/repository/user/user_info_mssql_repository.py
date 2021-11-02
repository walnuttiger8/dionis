from domain import UserInfo, IUserInfoRepository, IUserInfoDao
from infrastructure.repository.base import MSSQLRepository


class UserInfoMSSQLRepository(MSSQLRepository[UserInfo], IUserInfoRepository):

    def __init__(self, user_info_dao: IUserInfoDao):
        super().__init__(user_info_dao)

    def get_from_user_id(self, user_id: int) -> UserInfo:
        pass
