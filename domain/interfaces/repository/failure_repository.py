from domain.entities.failure import Failure
from domain.interfaces.repository.base import IRepository
from abc import ABC


class IFailureRepository(IRepository[Failure], ABC):
    pass
