from celery import shared_task

from TextCategorization.services.categorization import Categorization


@shared_task(queue='celery_1')
def get_categories_task(content):
    return Categorization.get_categories(content)
