from abc import abstractmethod, ABCMeta
from .db_command import IDbCommand


class IDbConnection(metaclass=ABCMeta):

    @abstractmethod
    def execute_command(self, db_command: IDbCommand) -> None | list:
        pass
