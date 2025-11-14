import logging
from django.db.models.signals import post_save
from django.dispatch import receiver
from notes.models import Note

logger = logging.getLogger(__name__)

@receiver(post_save, sender=Note)
def notify_note_created(sender, instance, created, **kwargs):
    if created:
        logger.info(f"用戶 {instance.author} 已建立 {instance.title}")