from django.shortcuts import get_object_or_404, render

from .models import MediaItem


def media_list(request):
    items = MediaItem.objects.all()
    return render(request, "media/media_list.html", {"items": items})


def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    return render(request, "media/media_detail.html", {"item": item})

# Create your views here.
