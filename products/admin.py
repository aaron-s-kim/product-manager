from django.contrib import admin
from .models import Category, Tag, Product


# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at")
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "price", "quantity", "created_at")
    list_filter = ("category", "tags")
    search_fields = ("name", "description")
    filter_horizontal = ("tags",)  # For better many-to-many field handling
    ordering = ("-created_at",)
