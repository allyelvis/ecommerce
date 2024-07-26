# invoices/views.py

from django.shortcuts import render, redirect
from .forms import InvoiceForm
from .models import Invoice

def create_invoice(request):
    if request.method == 'POST':
        form = InvoiceForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('invoice_list')
    else:
        form = InvoiceForm()
    return render(request, 'ecommerce_app/invoices/templates/invoices/invoice_form.html', {'form': form})

def invoice_list(request):
    invoices = Invoice.objects.all()
    return render(request, 'ecommerce_app/invoices/templates/invoices/invoice_list.html', {'invoices': invoices})
