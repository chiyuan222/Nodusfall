from django.db.models import Q
from django.shortcuts import render

from media.models import MediaItem
from wiki.models import WikiPage

from .models import FeaturedItem, HomeSlide, OfficialLink


def home(request):
    slides = HomeSlide.objects.filter(is_active=True)
    featured = FeaturedItem.objects.filter(is_active=True)
    official_links = OfficialLink.objects.all()
    latest_pages = WikiPage.objects.filter(status="published")[:8]
    latest_videos = MediaItem.objects.all()[:8]
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


def search_view(request):
    q = request.GET.get("q", "").strip()
    pages = []
    videos = []
    if q:
        pages = WikiPage.objects.filter(status="published").filter(
            Q(title__icontains=q) | Q(content_md__icontains=q)
        )
        videos = MediaItem.objects.filter(
            Q(title__icontains=q) | Q(author_name__icontains=q)
        )
    return render(request, "core/search.html", {"q": q, "pages": pages, "videos": videos})

# Create your views here.
