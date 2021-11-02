from domain import IFailureRepository, Failure, ISpecification, IFailureDao


class FailureRepository(IFailureRepository):

    def __init__(self, dao: IFailureDao):
        self._dao = dao

    def add(self, failure: Failure) -> Failure:
        return self._dao.create(failure)

    def get(self, failure_id: int) -> Failure:
        return self._dao.read(failure_id)

    def all(self) -> list[Failure]:
        pass

    def remove(self, failure_id: int) -> None:
        pass

    def filter(self, specifications: list[ISpecification]) -> list[Failure]:
        pass

    def update(self, failure: Failure) -> None:
        pass
