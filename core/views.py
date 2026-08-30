from django.shortcuts import render

from media.models import MediaItem
from wiki.models import WikiPage

from .models import FeaturedItem, HomeSlide, OfficialLink


def home(request):
    slides = HomeSlide.objects.filter(is_active=True)
    featured = FeaturedItem.objects.filter(is_active=True)
    official_links = OfficialLink.objects.all()
    latest_pages = WikiPage.objects.filter(status="published")[:10]
    latest_videos = MediaItem.objects.all()[:10]
    return render(
        request,
        "core/home.html",
        {
            "slides": slides,
            "featured": featured,
            "official_links": official_links,
            "latest_pages": latest_pages,
            "latest_videos": latest_videos,
        },
    )

# Create your views here.
