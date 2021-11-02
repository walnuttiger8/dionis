from domain import User, Failure, CreateFailureRequest, CreateFailureUseCase, UpdateFailureUseCase, UpdateFailureRequest, UserAccount
from infrastructure import UserRepository, FailureRepository, FailureTextDao
from infrastructure.dao.user import UserAccountMSSQLDao

from infrastructure.dao.user.user_mssql_dao import UserMSSQLDao
from infrastructure.utils.connection.db.connections import MSSqlConnection


def test():
    user_data = {
        "id": 1,
        "name": "Test",
    }

    failure_data = {
        "id": 1,
        "name": "First",
        "description": "First failure"
    }
    user = User(**user_data)
    failure = Failure(**failure_data)

    user_repo = UserRepository()
    failure_dao = FailureTextDao()
    failure_repo = FailureRepository(failure_dao)

    r = CreateFailureRequest(user, failure)
    u = CreateFailureUseCase(failure_repo, user_repo)
    update = UpdateFailureUseCase(failure_repo)

    u.execute(r)
    failure.description = "new description"
    update_request = UpdateFailureRequest(user, failure)
    update.execute(update_request)
    # print(user)
    # print(failure)

    print(failure_repo.get(1))


from typing import TypeVar, Generic

T = TypeVar("T")


class Test(Generic[T]):

    def __init__(self):
        self.et = T
        print("init")

    def do(self, obj: T):
        print("type:", self.et)


if __name__ == '__main__':
    user_data = {
        "id": 1,
        "name": "Test",
    }


    failure_data = {
        "id": 1,
        "name": "First",
        "description": "First failure"
    }
    user = User(**user_data)
    user_account = UserAccount(user_id=1, login="123", password_hash="pswhash")
    failure = Failure(**failure_data)

    # t: Test[User] = Test[User]()
    # print(Test[User])
    # print(t)
    # t.do(failure)
    # t.do(user)

    c = MSSqlConnection.TEST_DB.connect()
    d: UserAccountMSSQLDao = UserAccountMSSQLDao(c)
    d.init_table()
    u = d.create(user_account)
    print(u)
    # dao = UserMSSQLDao(c)
    # print(dao.create(User))
    # print(dao.read(1))
