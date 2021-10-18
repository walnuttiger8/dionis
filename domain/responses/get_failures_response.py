from domain.interfaces import IResponse
from domain.entities import Failure


class GetFailuresResponse(IResponse):
    def __init__(self, failures: list[Failure]):
        self._failures = failures

    @property
    def failures(self) -> list[Failure]:
        return self._failures
