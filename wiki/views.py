from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from .forms import PageForm
from .models import PageRevision, WikiPage


def page_list(request):
    pages = WikiPage.objects.filter(status="published")
    return render(request, "wiki/page_list.html", {"pages": pages})


def worldview(request):
    pages = WikiPage.objects.filter(
        status="published", categories__category__slug="worldview"
    ).distinct()
    return render(request, "wiki/worldview.html", {"pages": pages})


def page_detail(request, namespace, slug):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug, status="published")
    return render(request, "wiki/page_detail.html", {"page": page})


def _render_edit(request, page, form):
    return render(
        request,
        "wiki/page_edit.html",
        {
            "form": form,
            "page": page,
            "preview_source": request.POST.get("content_md", ""),
        },
    )


@login_required
def page_create(request):
    form = PageForm(request.POST or None)
    if request.method == "POST":
        if "preview" in request.POST and form.is_valid():
            return _render_edit(request, None, form)
        if form.is_valid():
            page = form.save()
            PageRevision.objects.create(
                page=page,
                content_md=page.content_md,
                summary=form.cleaned_data.get("summary") or "创建词条",
                editor=request.user,
            )
            return redirect("wiki:page_detail", namespace=page.namespace, slug=page.slug)
    return render(request, "wiki/page_edit.html", {"form": form, "page": None})


@login_required
def page_edit(request, namespace, slug):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug)
    form = PageForm(request.POST or None, instance=page)
    if request.method == "POST":
        if "preview" in request.POST and form.is_valid():
            return _render_edit(request, page, form)
        if form.is_valid():
            form.save()
            PageRevision.objects.create(
                page=page,
                content_md=page.content_md,
                summary=form.cleaned_data.get("summary") or "更新词条",
                editor=request.user,
            )
            return redirect("wiki:page_detail", namespace=page.namespace, slug=page.slug)
    return render(request, "wiki/page_edit.html", {"form": form, "page": page})


def page_history(request, namespace, slug):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug)
    revisions = page.revisions.all()
    return render(request, "wiki/page_history.html", {"page": page, "revisions": revisions})


def page_revision_detail(request, namespace, slug, revision_id):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug)
    revision = get_object_or_404(PageRevision, pk=revision_id, page=page)
    return render(
        request, "wiki/page_revision_detail.html", {"page": page, "revision": revision}
    )


@login_required
def page_revert(request, namespace, slug, revision_id):
    page = get_object_or_404(WikiPage, namespace=namespace, slug=slug)
    revision = get_object_or_404(PageRevision, pk=revision_id, page=page)
    if request.method == "POST":
        PageRevision.objects.create(
            page=page,
            content_md=revision.content_md,
            summary=f"回滚到修订 #{revision.pk}",
            editor=request.user,
        )
        page.content_md = revision.content_md
        page.save()
        return redirect("wiki:page_detail", namespace=page.namespace, slug=page.slug)
    return redirect(
        "wiki:page_revision_detail",
        namespace=namespace,
        slug=slug,
        revision_id=revision_id,
    )

# Create your views here.
