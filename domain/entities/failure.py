from pydantic import BaseModel


class Failure(BaseModel):
    id: int
    name: str
    description: str
    creator: type('User') = None
