from domain import UserAccount
from domain.interfaces.dao.user_account_dao import IUserAccountDao
from infrastructure.dao.base import MSSQLDao
from infrastructure.dao.base.mssql_dao import T
from infrastructure.utils.connection.db import MSSQLCommand, MSSqlConnection


class UserAccountMSSQLDao(MSSQLDao[UserAccount], IUserAccountDao):

    def all(self) -> list[T]:
        pass

    def __init__(self, db: MSSqlConnection):
        super().__init__(db, UserAccount)

    @property
    def table_name(self) -> str:
        return "UserAccount"

    @property
    def user_table_name(self):
        return "Users"

    def init_table(self):
        # language=SQL
        query = f"""
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='{self.table_name}' AND XTYPE='U')
            CREATE TABLE {self.table_name} (
            id INT PRIMARY KEY IDENTITY,
            user_id INT REFERENCES {self.user_table_name} (id), 
            login NVARCHAR(120),
            password_hash NVARCHAR(255) 
            )
        """
        command = MSSQLCommand(query)
        self.db.execute_command(command)

    def create(self, entity: UserAccount) -> UserAccount:
        # language=SQL
        query = f"""
        INSERT INTO {self.table_name}
        (user_id, login, password_hash)
        OUTPUT INSERTED.*
        VALUES({entity.user_id}, '{entity.login}', '{entity.password_hash}')
        """
        command = MSSQLCommand(query)
        output = self.db.execute_command(command)
        return UserAccount(**output[0])

    def update(self, entity: T) -> None:
        pass