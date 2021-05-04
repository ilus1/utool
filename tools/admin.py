from django.contrib import admin
from .models import Category, Tool
from .forms import NewTool

@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "slug", "created", "modified"]


@admin.register(Tool)

class ToolAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "slug",
        "category",
        "price",
        "is_available",
        "created",
        "modified",
        "owner",
    ]
    list_filter = ["is_available", "created", "modified"]
    list_editable = ["price", "is_available"]
