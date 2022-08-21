from django.core.mail import send_mail

import config.settings


def send(user_email, title, status):
    send_mail(
        subject=f'Your ticket ({title}) changed status',
        message=f'Status: {status}',
        from_email=config.settings.EMAIL_ADDRESS,
        recipient_list=[user_email],
        fail_silently=False
    )
