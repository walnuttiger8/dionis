from domain import UserAccount, IUserAccountRepository
from domain.interfaces.dao.user_account_dao import IUserAccountDao
from infrastructure.repository.base import MSSQLRepository


class UserAccountMSSQLRepository(MSSQLRepository[UserAccount], IUserAccountRepository):

    def __init__(self, user_account_dao: IUserAccountDao):
        self.user_account_dao = user_account_dao
        super().__init__(self.user_account_dao)

    def get_from_user_id(self, user_id: int) -> UserAccount:
        return self.user_account_dao.from_user_id(user_id)

    def get_from_login(self, login: str) -> UserAccount:
        return self.user_account_dao.from_login(login)
