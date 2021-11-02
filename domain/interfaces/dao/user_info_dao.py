from abc import ABC

from domain.entities import UserInfo
from domain.interfaces.dao.base import IDao


class IUserInfoDao(IDao[UserInfo], ABC):
    pass
