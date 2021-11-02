from domain.interfaces.dao import IUserInfoDao
from domain.entities import UserInfo
from infrastructure.dao.base import MSSQLDao
from infrastructure.dao.base.mssql_dao import T
from infrastructure.utils.connection.db.commands import MSSQLCommand


class UserInfoMSSQLDao(MSSQLDao[UserInfo], IUserInfoDao):
    @property
    def table_name(self) -> str:
        return "UserInfo"

    @property
    def user_table_name(self):
        return "Users"

    def init_table(self):
        # language=SQL
        query = f"""
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE NAME='{self.table_name}' AND XTYPE='U')
            CREATE TABLE {self.table_name}
            (
            id INT PRIMARY KEY IDENTITY,
            user_id INT REFERENCES {self.user_table_name} (id), 
            first_name NVARCHAR(120),
            last_name NVARCHAR(120),
            middle_name NVARCHAR(120) null,
            birthday DATE NULL
            )
        """
        command = MSSQLCommand(query)
        self.db.execute_command(command)

    def create(self, entity: UserInfo) -> UserInfo:
        # language=SQL
        query = f"""
        INSERT INTO {self.table_name} 
        (user_id, first_name, last_name, middle_name, birthday)
        OUTPUT INSERTED.*
        VALUES({entity.user_id}, '{entity.first_name}', '{entity.last_name}', '{entity.middle_name}', 
        '{entity.birthday}')
        """
        command = MSSQLCommand(query)
        output = self.db.execute_command(command)
        return self.entity_type(**output[0])

    def from_user_id(self, user_id: int) -> UserInfo | None:
        # language=SQL
        query = f"""
        select top 1 *
        from {self.table_name}
        where user_id = {user_id}
        """
        command = MSSQLCommand(query)
        output = self.db.execute_command(command)
        if output:
            return UserInfo(**output[0])

    def update(self, entity: T) -> None:
        pass

    def get_from_user_id(self, user_id: int) -> UserInfo:
        pass
