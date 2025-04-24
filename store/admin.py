from django.contrib import admin
from .models import UserProfile
admin.site.register(UserProfile)
from .models import Category, Product, Wishlist

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Wishlist)