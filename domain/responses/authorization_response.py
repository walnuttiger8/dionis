from domain import User, IResponse


class AuthorizationResponse(IResponse):
    def __init__(self, user: User):
        self._user = user

    @property
    def user(self):
        return self._user
