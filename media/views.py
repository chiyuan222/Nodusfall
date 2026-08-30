from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import MediaItemForm
from .models import MediaItem
from .parser import parse_media_url


def media_list(request):
    items = MediaItem.objects.all()
    return render(request, "media/media_list.html", {"items": items})


def media_detail(request, pk):
    item = get_object_or_404(MediaItem, pk=pk)
    return render(request, "media/media_detail.html", {"item": item})


@login_required
def media_add(request):
    form = MediaItemForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        parsed = parse_media_url(form.cleaned_data["url"])
        if not parsed:
            form.add_error("url", "无法识别该链接，请检查是否为 B 站视频或 YouTube 链接")
        else:
            provider, video_id = parsed
            item = MediaItem.objects.create(
                provider=provider,
                video_id=video_id,
                source_url=form.cleaned_data["url"],
                title=form.cleaned_data["title"] or video_id,
                category=form.cleaned_data["category"],
                author_name=form.cleaned_data["author_name"],
                language=form.cleaned_data["language"] or "zh",
                license_note=form.cleaned_data["license_note"],
                created_by=request.user,
            )
            return redirect("media:media_detail", pk=item.pk)
    return render(request, "media/media_add.html", {"form": form})

# Create your views here.
