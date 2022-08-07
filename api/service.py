from django.core.mail import send_mail


def send(user_email, title, status):
    send_mail(
        subject='Your task status changed!',
        message=f'Ticket: {title} | Status: {status}',
        from_email='admin@helpdesk.com',
        recipient_list=[user_email],
        fail_silently=False
    )

