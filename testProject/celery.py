from __future__ import absolute_import, unicode_literals
import os
from celery import Celery
import logging

logger = logging.getLogger(__name__)

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'testProject.settings')

app = Celery('testProject', broker='redis://127.0.0.1:6379')

app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')



# calculate avrage Rate 
from blog.models import rateModel,contentModel
from django.db.models import Sum
from celery import shared_task


@app.task(bind=True)
def calculateAvrageRate(self,contentID):
    instnce = rateModel.objects.filter(content__id = contentID)
    numberOfRates = instnce.count()
    averageRate = instnce.aggregate(Sum('rate'))['rate__sum']/numberOfRates
    contentObj = contentModel.objects.get(id= contentID)
    contentObj.numberOfRates  = numberOfRates 
    contentObj.averageRate  = averageRate
    contentObj.save()
    return "task Done"





    