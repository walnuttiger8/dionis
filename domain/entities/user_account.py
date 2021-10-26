from pydantic import BaseModel


class UserAccount(BaseModel):
    """
    Entity for authorization and registration
    """
    id: int
    user_id: int
    login: str
    password_hash: str
