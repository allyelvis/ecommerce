# invoices/admin.py

from django.contrib import admin
from .models import Invoice

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer_name', 'total_amount', 'date_created')
    search_fields = ('invoice_number', 'customer_name')
    list_filter = ('date_created',)
    ordering = ('-date_created',)

admin.site.register(Invoice, InvoiceAdmin)
