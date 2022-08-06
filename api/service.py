from django.core.mail import send_mail


def send(user_email):
    send_mail(
        subject='HelpDesk status tracker',
        message='Your task status is OK',
        from_email='admin@helpdesk.com',
        recipient_list=[user_email],
        fail_silently=False
    )
    print('email')
