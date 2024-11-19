from fastapi import APIRouter
from my_app_new.background_tasks.celery_task import send_email

router = APIRouter(prefix="/email")


@router.get("/")
def get_mess_email():
    send_email.delay()
    return {
        'status': 200,
        'data': 'письмо отправлено',
        'details': None
    }
