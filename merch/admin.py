from django.contrib import admin
from merch.models import Product,Category,Payment

# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Payment)
