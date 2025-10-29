from django.contrib import admin
from .models import Note

# Register your models here.


@admin.register(Note)
class Noteadmin(admin.ModelAdmin):
    list_display = ["title", "content", "created_at", "author"]
    list_filter = ["title"]
    search_fields = ["author"]
    ordering = ["content"]
