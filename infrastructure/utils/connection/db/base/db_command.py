from abc import ABCMeta, abstractmethod


class IDbCommand(metaclass=ABCMeta):

    @abstractmethod
    def get_command(self) -> str:
        pass
