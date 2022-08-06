from api.celery import app
from api.service import send


@app.task
def send_email(user_email, status):
    send(user_email, status)
