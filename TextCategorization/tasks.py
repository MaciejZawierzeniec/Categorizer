from celery import shared_task

from TextCategorization.services.categorization import Categorization


@shared_task
def get_categories_task(content):
    return Categorization.get_categories(content)
