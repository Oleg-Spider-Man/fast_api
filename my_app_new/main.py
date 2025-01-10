import uvicorn
from fastapi import FastAPI, Request, BackgroundTasks
from starlette.middleware.cors import CORSMiddleware

from my_app_new.auth_.auth import auth_backend
from my_app_new.auth_.user_obj import fastapi_users
from my_app_new.background_tasks.func_backgroundtasks import write_notification
from my_app_new.routers import celery_email, authors, books
from my_app_new.auth_.schemas import UserRead, UserCreate

app = FastAPI(summary="здесь можно написать краткое описание приложения")

origins = [
    "http://localhost:8000",  # или адрес фронтенда
    "http://192.168.99.100:9998",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Важный флаг для работы с куками
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware('http')
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['header'] = 'header from middleware'
    return response


@app.post('/send-notification/{email}')
async def send_notification(email: str, background_tasks: BackgroundTasks):
    background_tasks.add_task(write_notification, email, message='some notification')
    return 'запись в файл проекта с помощью BackgroundTasks, для аутентифицированного user - выполнена!'

app.include_router(
    fastapi_users.get_auth_router(auth_backend),
    prefix="/auth_/jwt",
    tags=["auth_"],
)

app.include_router(
    fastapi_users.get_register_router(UserRead, UserCreate),
    prefix="/auth_",
    tags=["auth_"],
)

app.include_router(authors.router)
app.include_router(books.router)
app.include_router(celery_email.router)


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
