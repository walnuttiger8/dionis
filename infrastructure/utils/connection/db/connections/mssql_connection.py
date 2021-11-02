from infrastructure.utils.connection.db.base import IDbConnection
from infrastructure.utils.connection.db.commands.mssql_command import MSSQLCommand
from infrastructure.utils.connection.db.credentials import TestDbCredentials


class MSSQLConnection(IDbConnection):
    TEST_DB = TestDbCredentials()

    def __init__(self, connection):
        self._connection = connection
        self._cursor = self._connection.cursor(as_dict=True)

    def execute_command(self, db_command: MSSQLCommand) -> None | list:
        query = db_command.get_command()
        self._cursor.execute(query)

        output = []
        for row in self._cursor:
            output.append(row)
        return output
