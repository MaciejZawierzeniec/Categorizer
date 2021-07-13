from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<int:pk>/', views.DocumentDetailView.as_view(), name='document-details'),
    path('document_list/', views.DocumentListView.as_view(), name='document-list'),
    path('document_update/<int:pk>/', views.DocumentUpdateView.as_view(), name='document-update'),
    path('document_confirm_delete/<int:pk>/', views.DocumentDeleteView.as_view(), name='delete-document'),
]
