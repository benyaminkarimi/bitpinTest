from django.db.models import signals
from django.dispatch import receiver
from blog.models import rateModel
from testProject.celery import calculateAvrageRate

from blog.models import rateModel,contentModel
from django.db.models import Sum

@receiver(signals.post_save, sender=rateModel)
def signl(sender, instance, **kwargs):
    calculateAvrageRate.delay(instance.content.id)







