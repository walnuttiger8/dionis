from abc import abstractmethod, ABCMeta


class DbConnection(metaclass=ABCMeta):

    def __init__(self, connection_string):
        self.connection_string = None
