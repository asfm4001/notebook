import logging
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.contrib.auth.models import User

logger = logging.getLogger(__name__)

@receiver(user_logged_in, sender=User)
def notify_user_login(sender, request, user, **kwargs):
    # print(f"User {user.username} 已登入，IP：{request.META.get('REMOTE_ADDR')}")
    logger.info(f"User {user.username} 已登入，IP：{request.META.get('REMOTE_ADDR')}")