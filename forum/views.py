from django.shortcuts import get_object_or_404, render

from .models import Board


def forum_home(request):
    boards = Board.objects.filter(is_active=True)
    return render(request, "forum/forum_home.html", {"boards": boards})


def board_detail(request, slug):
    board = get_object_or_404(Board, slug=slug, is_active=True)
    return render(request, "forum/board_detail.html", {"board": board})

# Create your views here.
