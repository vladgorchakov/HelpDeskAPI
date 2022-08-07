from api.celery import app
from api.service import send


@app.task
def send_email(user_email, title, status):
    send(user_email, title, status)
