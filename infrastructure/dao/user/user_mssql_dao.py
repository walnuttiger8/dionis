from domain import User
from domain.interfaces import IUserDao
from infrastructure.dao.base import MSSQLDao
from infrastructure.dao.base.mssql_dao import T
from infrastructure.utils.connection.db import MSSQLCommand, MSSQLConnection


class UserMSSQLDao(MSSQLDao[User], IUserDao):

    def __init__(self, db: MSSQLConnection):
        super().__init__(db, User)

    @property
    def table_name(self) -> str:
        return "Users"

    def create(self, entity: T) -> User:
        # language=SQL
        query = f"""
        INSERT INTO {self.table_name}
        OUTPUT INSERTED.*
        DEFAULT VALUES
        """
        command = MSSQLCommand(query)
        result = self.db.execute_command(command)
        return User(**result[0])

    def update(self, entity: T) -> None:
        """
        should not be implemented
        :param entity:
        :return:
        """
        raise NotImplementedError()

    def init_table(self) -> None:
        # language=SQL
        query = f"""
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='{self.table_name}' AND XTYPE='U')
            CREATE TABLE {self.table_name}
            (
            id INT PRIMARY KEY IDENTITY
            )
        """
        command = MSSQLCommand(query)
        self.db.execute_command(command)
