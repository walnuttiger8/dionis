from abc import ABCMeta
from domain.entities.failure import Failure
from domain.interfaces.dao.base import IDao


class IFailureDao(IDao[Failure], metaclass=ABCMeta):
    pass
