from domain import IRequest


class AuthorizationRequest(IRequest):

    def __init__(self, login: str, password_hash: str):
        self._login = login
        self._password_hash = password_hash

    @property
    def login(self):
        return self._login

    @property
    def password_hash(self):
        return self._password_hash
