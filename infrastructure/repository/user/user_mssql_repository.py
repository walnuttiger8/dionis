from domain import IUserRepository
from infrastructure.dao.user import UserMSSQLDao
from infrastructure.repository.base import MSSQLRepository


class UserMSSQLRepository(MSSQLRepository, IUserRepository):

    def __init__(self, user_dao: UserMSSQLDao):
        super().__init__(user_dao)
