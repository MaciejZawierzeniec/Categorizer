from django import forms

from TextCategorization.models import Document


class DocumentForm(forms.ModelForm):
    class Meta:
        model = Document
        fields = ('title', 'document')
