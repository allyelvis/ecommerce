# ecommerce_app/urls.py

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ecommerce_app/invoices/templates/invoices/', include('invoices.urls')),
    path('', TemplateView.as_view(template_name="ecommerce/index.html"), name='home'),
]
