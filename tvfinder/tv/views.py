from django.shortcuts import render

from .models import Tv


def films(request):
    films_titles = Tv.objects.filter(tv_type='f')
    return render(request, 'tv/tv.html', {'all_tv': films_titles})


def series(request):
    series_titles = Tv.objects.filter(tv_type='s')
    return render(request, 'tv/tv.html', {'all_tv': series_titles})
