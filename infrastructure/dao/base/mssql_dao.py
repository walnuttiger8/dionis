from domain.interfaces.dao.base import IDao
from abc import abstractmethod, ABC
from typing import TypeVar

from infrastructure.utils.connection.db import MSSqlConnection, MSSqlCommand

T = TypeVar("T")


class MSSQLDao(IDao[T], ABC):

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    def __init__(self, db: MSSqlConnection):
        self._db = db

    @abstractmethod
    def create(self, entity: T) -> None:
        pass

    @abstractmethod
    def update(self, entity: T) -> None:
        pass

    def read(self, entity_id: int) -> T | None:
        # language=SQL
        query = f"""
        SELECT *
        FROM {self.table_name} 
        WHERE Id = {entity_id}
        """
        command = MSSqlCommand(query)
        result = self._db.execute_command(command)
        if not result:
            return
        return T(**result[0])

    def delete(self, entity_id: int) -> None:
        # language=SQL
        query = f"""
        DELETE *
        FROM {self.table_name} 
        WHERE Id = {entity_id}
        """
        command = MSSqlCommand(query)
        self._db.execute_command(command)
