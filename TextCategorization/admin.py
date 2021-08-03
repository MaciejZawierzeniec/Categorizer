from django.contrib import admin

from TextCategorization.models import Document


class DocumentAdmin(admin.ModelAdmin):
    fields = ('title', 'document', 'content', 'categories')
    readonly_fields = ['content', 'categories']


admin.site.register(Document, DocumentAdmin)
