from infrastructure.utils.connection.db.base import IDbCommand


class MSSQLCommand(IDbCommand):

    def __init__(self, query: str):
        self._query = query

    def __str__(self):
        return self._query

    def get_command(self) -> str:
        return self._query
