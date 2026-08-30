from django.shortcuts import render

from media.models import MediaItem
from wiki.models import WikiPage


def home(request):
    latest_pages = WikiPage.objects.filter(status="published")[:10]
    latest_videos = MediaItem.objects.all()[:10]
    return render(
        request,
        "core/home.html",
        {"latest_pages": latest_pages, "latest_videos": latest_videos},
    )

# Create your views here.
