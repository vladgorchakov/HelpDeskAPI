from api.celery import app
from api.service import send


@app.task
def send_email(user_email):
    send(user_email)
