from django.core.mail import send_mail
from config.settings import EMAIL_ADDRESS as email_address


def send(user_email, title, status):
    send_mail(
        subject=f'Your ticket ({title}) changed status',
        message=f'Status: {status}',
        from_email=email_address,
        recipient_list=[user_email],
        fail_silently=False
    )
