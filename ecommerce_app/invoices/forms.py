# invoices/forms.py

from django import forms
from .models import Invoice

class InvoiceForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = ['invoice_number', 'customer_name', 'customer_email', 'product_name', 'quantity', 'price', 'total']