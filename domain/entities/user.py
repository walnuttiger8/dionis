from pydantic import BaseModel


class User(BaseModel):
    id: int
    name: str
    created_failures: list[type('Failure')] = []

    def create_failure(self, failure):
        self.created_failures.append(failure)
        failure.creator = self
