from django.db import models

from TextCategorization.services.categorization import Categorization


class Document(models.Model):
    title = models.CharField(max_length=100, blank=True)
    document = models.FileField(upload_to='documents/')
    categories = models.CharField(max_length=255, default='')

    def __str__(self):
        return self.title

    @property
    def content(self):
        return self.document.read()

    def save(self, *args, **kwargs):
        self.categories = Categorization.get_categories(self.content)
        super(Document, self).save(*args, **kwargs)
