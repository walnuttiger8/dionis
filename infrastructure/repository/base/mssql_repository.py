from abc import ABC
from typing import TypeVar
from domain import ISpecification
from domain.interfaces import IRepository
from domain.interfaces.dao.base import IDao

T = TypeVar("T")


class MSSQLRepository(IRepository[T], ABC):
    dao: IDao

    def __init__(self, dao: IDao[T]):
        self.dao = dao

    def add(self, entity: T) -> T:
        return self.dao.create(entity)

    def get(self, entity_id: int) -> T:
        return self.dao.read(entity_id)

    def all(self) -> list[T]:
        return self.dao.all()

    def remove(self, entity_id: int) -> None:
        self.dao.delete(entity_id)

    def filter(self, specifications: list[ISpecification]) -> list[T]:
        return []

    def update(self, entity: T) -> None:
        self.dao.update(entity)
