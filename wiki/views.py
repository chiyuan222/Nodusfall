from django.shortcuts import get_object_or_404, render

from .models import WikiPage


def page_list(request):
    pages = WikiPage.objects.filter(status="published")
    return render(request, "wiki/page_list.html", {"pages": pages})


def page_detail(request, namespace, slug):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug, status="published")
    return render(request, "wiki/page_detail.html", {"page": page})

# Create your views here.
