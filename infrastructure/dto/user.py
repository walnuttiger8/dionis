from pydantic import BaseModel, Field


class UserDTO(BaseModel):
    id: int = Field(alias="Id")
