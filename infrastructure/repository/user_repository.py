from domain import IUserRepository, User, ISpecification


class UserRepository(IUserRepository):

    def __init__(self):
        self._users: list[User] = list()

    def get(self, user_id: int) -> User:
        pass

    def all(self) -> list[User]:
        return self._users

    def remove(self, user_id: int) -> None:
        pass

    def filter(self, specifications: list[ISpecification]) -> list[User]:
        pass

    def update(self, user: User) -> None:
        pass

    def add(self, user: User) -> None:
        self._users.append(user)
