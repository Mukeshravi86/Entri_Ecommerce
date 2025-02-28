
from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'image','details')  
    search_fields = ('name',)  
    list_filter = ('price',) 
    details_feild=()


admin.site.register(Product,ProductAdmin)

