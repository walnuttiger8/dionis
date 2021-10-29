from .db_connection import IDbConnection


class IDbCredentials:

    def connect(self) -> IDbConnection:
        pass
