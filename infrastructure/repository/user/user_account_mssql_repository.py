from domain import UserAccount, IUserAccountRepository
from domain.interfaces.dao.user_account_dao import IUserAccountDao
from infrastructure.repository.base import MSSQLRepository


class UserAccountMSSQLRepository(MSSQLRepository[UserAccount], IUserAccountRepository):

    def __init__(self, user_account_dao: IUserAccountDao):
        super().__init__(user_account_dao)

    def get_from_user_id(self, user_id: int) -> UserAccount:
        pass

    def get_from_login(self, login: str) -> UserAccount:
        pass
