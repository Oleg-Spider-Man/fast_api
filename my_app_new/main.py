from fastapi import FastAPI, Request, BackgroundTasks, Depends
from fastapi_users import FastAPIUsers
from my_app_new.auth.auth import auth_backend
from my_app_new.auth.manager import get_user_manager
from my_app_new.auth.models import User
from my_app_new.background_tasks.func_backgroundtasks import write_notification
from my_app_new.routers import celery_email
from my_app_new.auth.schemas import UserRead, UserCreate

app = FastAPI(summary="здесь можно написать краткое описание приложения")


fastapi_users = FastAPIUsers[User, int](
    get_user_manager,
    [auth_backend],
)

current_user = fastapi_users.current_user()


@app.middleware('http')
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['header'] = 'header from middleware'
    return response


@app.post('/send-notification/{email}', dependencies=[Depends(current_user)])
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message='some notification')
    return 'запись в файл проекта с помощью BackgroundTasks, для аутентифицированного user - выполнена!'

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth/jwt",
    tags=["auth"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth",
    tags=["auth"],
)

# app.include_router(users.router)
# app.include_router(items.router)
app.include_router(celery_email.router)
