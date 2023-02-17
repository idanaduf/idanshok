from django.contrib import admin

# Register your models here.
from .models import Product
from .models import Client






admin.site.register(Product)
admin.site.register(Client)




