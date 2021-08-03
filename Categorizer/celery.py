from __future__ import absolute_import, unicode_literals
import os

from celery import Celery

from Categorizer import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Categorizer.settings')
app = Celery('Categorizer', backend=settings.CELERY_RESULT_BACKEND, broker=settings.CELERY_BROKER_URL)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()

