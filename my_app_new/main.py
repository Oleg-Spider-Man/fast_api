from fastapi import FastAPI, Request
from my_app_new.routers import users, items

app = FastAPI(summary="здесь можно написать краткое описание приложения")


@app.middleware('http')
async def add_header(request: Request, call_next):
    response = await call_next(request)
    response.headers['Заголовок'] = 'из middleware добавленный'
    return response

app.include_router(users.router)
app.include_router(items.router)
