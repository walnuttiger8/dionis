from abc import ABC

from domain.entities import UserAccount
from domain.interfaces.dao.base import IDao


class IUserAccountDao(IDao[UserAccount], ABC):
    pass
