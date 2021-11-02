from pydantic import BaseModel


class UserAccount(BaseModel):
    """
    Entity for authorization and registration
    """
    id: int = None
    user_id: int = None
    login: str
    password_hash: str
