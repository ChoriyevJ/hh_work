from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from django.utils import timezone

from main.models import Vacancy
from main.choices import PublishChoice


@receiver(post_save, sender=Vacancy)
def pull_vacancy_published_date_and_time(sender, instance, created, **kwargs):
    if created:
        if instance.publish_type == PublishChoice.PUBLISH_NOW:
            instance.published_date = timezone.now().date()
            instance.published_time = timezone.now().time()
            instance.save()
    else:
        if not instance.published_date or not instance.published_time:
            instance.published_date = timezone.now().date()
            instance.published_time = timezone.now().time()
            instance.save()







