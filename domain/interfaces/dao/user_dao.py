from abc import ABC
from domain.entities.user import User
from domain.interfaces.dao.base import IDao


class IUserDao(IDao[User], ABC):
    pass
