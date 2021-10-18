from domain import User, Failure, CreateFailureRequest, CreateFailureUseCase
from infrastructure import UserRepository, FailureRepository, FailureTextDao

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
    failure = Failure(**failure_data)

    user_repo = UserRepository()
    failure_dao = FailureTextDao()
    failure_repo = FailureRepository(failure_dao)

    r = CreateFailureRequest(user, failure)
    u = CreateFailureUseCase(failure_repo, user_repo)

    u.execute(r)
    print(user)
    print(failure)
