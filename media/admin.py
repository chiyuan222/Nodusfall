from django.contrib import admin

from .models import MediaItem


@admin.register(MediaItem)
class MediaItemAdmin(admin.ModelAdmin):
    list_display = ("title", "provider", "category", "author_name", "language", "created_at")
    list_filter = ("provider", "category", "language")
    search_fields = ("title", "author_name", "video_id")
    filter_horizontal = ("pages",)

# Register your models here.
