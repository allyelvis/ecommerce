# invoices/models.py

from django.db import models

class Invoice(models.Model):
    invoice_number = models.CharField(max_length=100, unique=True)
    customer_name = models.CharField(max_length=100)
    customer_email = models.EmailField()
    product_name = models.CharField(max_length=100)
    quantity = models.PositiveIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.invoice_number