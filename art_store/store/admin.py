# store/admin.py

from django.contrib import admin
from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'price', 'stock', 'available', 'image')  # Display fields in the list view
    search_fields = ('name', 'category__name')  # Enable search by name and category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug')  # Display category name and slug
    prepopulated_fields = {'slug': ('name',)}  # Automatically generate slug from name

admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
