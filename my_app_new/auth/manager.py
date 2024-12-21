from typing import Optional
from my_app_new.auth.models import User
from fastapi import Depends, Request
from fastapi_users import BaseUserManager, IntegerIDMixin
from my_app_new.auth.func import get_user_db
from my_app_new.config import SECRET_AUTH_MNG


class UserManager(IntegerIDMixin, BaseUserManager[User, int]):
    reset_password_token_secret = SECRET_AUTH_MNG
    verification_token_secret = SECRET_AUTH_MNG

    async def on_after_register(self, user: User, request: Optional[Request] = None):
        print(f"User {user.id} has registered.")


async def get_user_manager(user_db=Depends(get_user_db)):
    yield UserManager(user_db)
