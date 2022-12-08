


# def check_birthday():
#     # проверять дни рождения, отправлять письмо
#     activation_link = f'http://3.92.183.40/api/account/activate/{activation_code}/'
#     html_message = render_to_string(
#         'account/code_mail.html',
#         {'activation_link': activation_link}
#         )
#     send_mail(
#         'Активируйте ваш аккаунт!',
#         '',
#         settings.EMAIL_HOST_USER,
#         [email],
#         html_message=html_message,
#         fail_silently=False   
#     )

import logging
 
from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from config.celery import app
from .models import UserProfile
from django.utils import timezone
from django.conf import settings
from config.celery import app
from django.core.mail import send_mail
from django.template.loader import render_to_string
from celery import shared_task
 
format = '%d.%m.%Y'
 
@shared_task(name='check_birthday')
def check_birthday():
    users = UserProfile.objects.all()
    for user in users:
        birthday = user.birthday.strptime(format)[:5]
        today = timezone.now().date().strptime(format)[:5]
        if birthday == today:
            print(birthday)
            print(today)
            print(birthday == today)
            html_message = render_to_string(
            'bio/birthday.html',
            )
            send_mail(
                'Поздравляем вас с днем рождения!',
                '',
                settings.EMAIL_HOST_USER,
                [user.user_profile.email],
                html_message=html_message,
                fail_silently=False   
        )


        # except UserModel.DoesNotExist:
        #     logging.warning("Tried to send verification email to non-existing user '%s'" % user_id)



# from django.core.management import BaseCommand
# from django.core.mail import send_mail
# from django.utils import timezone
# from someplace import User



# class Command(BaseCommand):
#     def handle(self, **options):
#         today = timezone.now().date()
#         for user in User.objects.filter(birth_date__day=today.day, birth_date__month=today.month):
#             subject = 'Happy birthday %s!' % user.first_name
#             body = 'Hi %s,\n...' + user.first_name
#             send_mail(subject, body, 'contact@yourdomain.com', [user.email])