from starlette.middleware.cors import CORSMiddleware
from my_app_new.main import app

origins = [
    "http://localhost:8000",  # или адрес фронтенда
    "http://192.168.99.100:9998",  # я использую Docker Toolbox, это для JWT из кук браузера
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,  # Важный флаг для работы с куками
    allow_methods=["*"],
    allow_headers=["*"],
)

