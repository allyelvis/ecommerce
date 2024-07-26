# invoices/urls.py

from django.urls import path
from .views import create_invoice, invoice_list

urlpatterns = [
    path('create/', create_invoice, name='create_invoice'),
    path('', invoice_list, name='invoice_list'),
]