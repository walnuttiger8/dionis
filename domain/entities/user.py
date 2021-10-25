from pydantic import BaseModel

from domain.entities import Failure


class User(BaseModel):
    id: int
    name: str
    created_failures: list[Failure] = []

    def create_failure(self, failure):
        self.created_failures.append(failure)
        failure.creator_id = self.id

    def delete_failure(self, failure: Failure):
        if failure in self.created_failures:
            self.created_failures.remove(failure)
