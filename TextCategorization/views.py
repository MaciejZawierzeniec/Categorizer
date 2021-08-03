from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from TextCategorization.models import Document


class DocumentCreateView(CreateView):
    model = Document
    fields = ['title', 'document']
    success_url = reverse_lazy('document-list')


class DocumentDetailView(DetailView):
    model = Document
    queryset = Document.objects.all()


class DocumentListView(ListView):
    model = Document


class DocumentUpdateView(UpdateView):
    model = Document
    fields = ['title', 'document']
    success_url = reverse_lazy('document-list')


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('document-list')
