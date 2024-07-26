# invoices/admin.py

from django.contrib import admin
from .models import Invoice, InvoiceItem

class InvoiceItemInline(admin.TabularInline):
    model = InvoiceItem
    extra = 1

class InvoiceAdmin(admin.ModelAdmin):
    list_display = ('invoice_number', 'customer_name', 'total_amount', 'date_created')
    search_fields = ('invoice_number', 'customer_name')
    inlines = [InvoiceItemInline]

admin.site.register(Invoice, InvoiceAdmin)