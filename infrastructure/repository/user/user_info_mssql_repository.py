from domain import UserInfo, IUserInfoRepository, IUserInfoDao
from infrastructure.repository.base import MSSQLRepository


class UserInfoMSSQLRepository(MSSQLRepository[UserInfo], IUserInfoRepository):

    def __init__(self, user_info_dao: IUserInfoDao):
        self.user_info_dao = user_info_dao
        super().__init__(user_info_dao)

    def get_from_user_id(self, user_id: int) -> UserInfo:
        return self.user_info_dao.from_user_id(user_id)
