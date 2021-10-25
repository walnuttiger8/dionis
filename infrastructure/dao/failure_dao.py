from domain import IFailureDao, Failure


class FailureTextDao(IFailureDao):

    def __init__(self):
        self._filename = "failure.txt"
        self._mode = "a+"

    def create(self, failure: Failure) -> None:
        with open(self._filename, self._mode) as f:
            f.write(failure.json())
            f.write("\n")

    def read(self, failure_id: int) -> Failure | None:
        with open(self._filename) as f:
            for data in f.readlines():
                failure = Failure.parse_raw(data)
                if failure.id == failure_id:
                    return failure

    def update(self, failure: Failure) -> None:
        pass

    def delete(self, failure_id) -> None:
        pass
