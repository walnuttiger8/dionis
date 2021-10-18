from domain import IFailureDao, Failure


class FailureTextDao(IFailureDao):

    def __init__(self):
        self._filename = "failure.txt"
        self._mode = "a+"

    def create(self, failure: Failure) -> None:
        with open(self._filename, self._mode) as f:
            f.write(failure.name)
            f.write("\n")

    def read(self, failure_id: int) -> Failure | None:
        pass

    def update(self, failure: Failure) -> None:
        pass

    def delete(self, failure_id) -> None:
        pass
