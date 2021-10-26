from datetime import date
from pydantic import BaseModel


class UserInfo(BaseModel):
    id: int
    user_id: int
    first_name: str
    last_name: str
    middle_name: str = ""
    birthday: date = None
