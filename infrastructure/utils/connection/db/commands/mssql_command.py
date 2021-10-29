from infrastructure.utils.connection.db.base import IDbCommand


class MSSqlCommand(IDbCommand):

    def __init__(self, query: str):
        self._query = query

    def get_command(self) -> str:
        return self._query
