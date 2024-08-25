from django.core.mail import send_mail

from config.celery import app


@app.task
def send_email(fullname, email):
    send_mail(
        'Subscription expired',
        f'Dear {fullname},Your subscription has expired',
        'support@quera.com',
        [email],
        fail_silently=True,
    )
