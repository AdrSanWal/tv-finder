from django.shortcuts import render

from .models import Tv, Director, Gender


def films(request):
    films_titles = Tv.objects.filter(tv_type='f')
    return render(request, 'tv/tv.html', {'all_tv': films_titles})


def series(request):
    series_titles = Tv.objects.filter(tv_type='s')
    return render(request, 'tv/tv.html', {'all_tv': series_titles})


def filtered_film(request, filter_type, filter_id):
    filtered_film = Tv.objects.get(id=filter_id)
    filter_type = filtered_film.tv_type
    directors = Director.objects.filter(directors__in=[filter_id])
    genders = Gender.objects.filter(genders__in=[filter_id])
    return render(request, 'tv/film.html', {'filtered_film': filtered_film,
                                            'genders': genders,
                                            'directors': directors})
