from domain import User, Failure, CreateFailureRequest, CreateFailureUseCase, UpdateFailureUseCase, \
    UpdateFailureRequest, UserAccount, RegisterUserRequest, UserInfo
from domain.use_cases.register_user import RegisterUserUseCase
from infrastructure import FailureRepository, FailureTextDao, UserInfoMSSQLRepository, UserAccountMSSQLRepository, \
    UserMSSQLRepository
from infrastructure.dao.user import UserAccountMSSQLDao, UserInfoMSSQLDao

from infrastructure.dao.user.user_mssql_dao import UserMSSQLDao
from infrastructure.utils.connection.db.connections import MSSQLConnection


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


def test_register():
    user_account_data = {
        "login": "second_login",
        "password_hash": "nu_tipa-pa$$word_ha$h))"
    }

    user_info_data = {
        "first_name": "Test",
        "last_name": "Testin",
        "middle_name": "Test ogli",
    }
    connection = MSSQLConnection.TEST_DB.connect()

    user_info_dao = UserInfoMSSQLDao(connection)
    user_account_dao = UserAccountMSSQLDao(connection)
    user_dao = UserMSSQLDao(connection)

    user_info_repository = UserInfoMSSQLRepository(user_info_dao)
    user_account_repository = UserAccountMSSQLRepository(user_account_dao)
    user_repository = UserMSSQLRepository(user_dao)

    user_account = UserAccount.parse_obj(user_account_data)
    user_info = UserInfo.parse_obj(user_info_data)

    request = RegisterUserRequest(user_account=user_account, user_info=user_info)
    use_case = RegisterUserUseCase(user_info_repository, user_account_repository, user_repository)

    response = use_case.execute(request)
    print(response)


if __name__ == '__main__':
    test_register()
