from django.urls import path
from .views import document_list, document_detail

urlpatterns = [
    path('document/', document_list, name='document_list'),
    path('document/<int:pk>/', document_detail, name='document_detail'),
]
