import smtplib
from email.message import EmailMessage
from celery import Celery
from my_app_new.config import SMTP_USER, SMTP_PASSWORD, REDIS_HOST, REDIS_PORT

celery_app = Celery('tasks', broker=f'redis://{REDIS_HOST}:{REDIS_PORT}')

SMTP_HOST = 'smtp.mail.ru'
SMTP_PORT = 465


def get_email():
    email = EmailMessage()
    email['Subject'] = 'Отправил сообщение'
    email['From'] = SMTP_USER
    email['To'] = SMTP_USER
    email.set_content(
        '<div>'
        f'<h1 style="color: red;">Привет из апи.</h1>'
        '<div>',
        subtype='html'
    )
    return email


@celery_app.task
def send_email():
    email = get_email()
    with smtplib.SMTP_SSL(SMTP_HOST, SMTP_PORT) as server:
        server.login(SMTP_USER, SMTP_PASSWORD)
        server.send_message(email)
        return "ok"
