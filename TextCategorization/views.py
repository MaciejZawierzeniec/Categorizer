from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView

from TextCategorization.forms import DocumentForm
from TextCategorization.models import Document


def index(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = DocumentForm()
    return render(request, 'TextCategorization/index.html', {
        'form': form,
        'documents': Document.objects.all()
    })


class DocumentDetailView(DetailView):

    model = Document
    queryset = Document.objects.all()


class DocumentListView(ListView):

    model = Document


class DocumentUpdateView(UpdateView):
    model = Document
    fields = ['title', 'document']
    template_name_suffix = '_update'
    success_url = reverse_lazy('document-list')


class DocumentDeleteView(DeleteView):
    model = Document
    success_url = reverse_lazy('document-list')
