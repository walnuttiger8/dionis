from domain import User
from domain.interfaces import IUserDao
from infrastructure.dao.base import MSSQLDao
from infrastructure.dao.base.mssql_dao import T
from infrastructure.utils.connection.db import MSSqlCommand


class UserMSSQLDao(MSSQLDao[User], IUserDao):

    @property
    def table_name(self) -> str:
        return "Users"

    def create(self, entity: T) -> None:
        pass

    def update(self, entity: T) -> None:
        pass

    def init_table(self) -> None:
        # language=SQL
        query = f"""
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='{self.table_name}' AND XTYPE='U')
            CREATE TABLE {self.table_name}
            (
            id INT PRIMARY KEY IDENTITY
            )
        """
        command = MSSqlCommand(query)
        self._db.execute_command(command)
