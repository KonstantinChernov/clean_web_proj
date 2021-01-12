from django.contrib import admin
from .models import Product, User, Cart, Type, Wishlist
# Register your models here.


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'discount', 'price_sale', 'type')
    list_display_links = ('name', 'price', 'discount', 'price_sale', 'type')


admin.site.register(Product, ProductAdmin)
admin.site.register(User)
admin.site.register(Cart)
admin.site.register(Type)
admin.site.register(Wishlist)