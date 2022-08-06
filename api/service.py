from django.core.mail import send_mail


def send(user_email, status):
    send_mail(
        subject='Your task status changed',
        message=f'Current status: {status}',
        from_email='admin@helpdesk.com',
        recipient_list=[user_email],
        fail_silently=False
    )
    print('email')
