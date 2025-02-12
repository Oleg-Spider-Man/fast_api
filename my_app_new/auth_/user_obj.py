from fastapi_users import FastAPIUsers
from my_app_new.auth_.auth import auth_backend
from my_app_new.auth_.manager import get_user_manager
from my_app_new.auth_.models import User

fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)


current_user = fastapi_users.current_user()
