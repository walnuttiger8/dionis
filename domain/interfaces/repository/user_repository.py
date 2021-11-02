from domain.entities.user import User
from domain.interfaces.repository.base import IRepository
from abc import ABC


class IUserRepository(IRepository[User], ABC):
    pass
