import time

from celery.result import AsyncResult
from django.db import models, transaction

from Categorizer.celery import app
from TextCategorization.services.categorization import Categorization
from TextCategorization.tasks import get_categories_task


class Document(models.Model):
    title = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='documents/')
    categories = models.CharField(max_length=255, default='', blank=True, null=True)

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self.document.read()

    def save(self, *args, **kwargs):
        result = get_categories_task.delay(str(self.content))
        self.categories = result.get()
        super(Document, self).save(*args, **kwargs)
