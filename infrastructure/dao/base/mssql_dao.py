from domain.interfaces.dao.base.dao import IDao, T
from abc import abstractmethod, ABC

from infrastructure.utils.connection.db import MSSQLConnection, MSSQLCommand


class MSSQLDao(IDao[T], ABC):
    entity_type: type

    @property
    @abstractmethod
    def table_name(self) -> str:
        pass

    def __init__(self, db: MSSQLConnection, entity_type: type):
        self.db = db
        self.entity_type = entity_type

    @abstractmethod
    def create(self, entity: T) -> T:
        pass

    def all(self):
        # language=SQL
        query = f"""
        SELECT *
        FROM {self.table_name}
        """
        command = MSSQLCommand(query)
        output = self.db.execute_command(command)
        return list(map(lambda e: self.entity_type(**e), output))

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
        command = MSSQLCommand(query)
        result = self.db.execute_command(command)
        if not result:
            return
        return self.entity_type(**result[0])

    def delete(self, entity_id: int) -> None:
        # language=SQL
        query = f"""
        DELETE *
        FROM {self.table_name} 
        WHERE id = {entity_id}
        """
        command = MSSQLCommand(query)
        self.db.execute_command(command)
