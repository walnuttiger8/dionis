from datetime import date
from pydantic import BaseModel


class UserInfo(BaseModel):
    id: int = None
    user_id: int = None
    first_name: str
    last_name: str
    middle_name: str = ""
    birthday: date = None
