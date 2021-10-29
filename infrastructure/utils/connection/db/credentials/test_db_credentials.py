from infrastructure.utils.connection.db.base import IDbCredentials
import pymssql


class TestDbCredentials(IDbCredentials):

    def __init__(self):
        self._server = r"DESKTOP-K70ACOB\SQLEXPRESS"
        self._database = "test_db"
        self._login_timeout = 5
        self._autocommit = True

    def connect(self):
        from infrastructure.utils.connection.db.connections import MSSqlConnection
        connection = pymssql.connect(server=self._server, database=self._database, login_timeout=self._login_timeout,
                                     autocommit=self._autocommit)
        return MSSqlConnection(connection)
