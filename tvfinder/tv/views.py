from django.shortcuts import render

from .models import Tv, Director, Gender


def filter_films(request, film_type):
    finder = request.GET.get('finder')
    if finder != '' and finder is not None:
        filtered = Tv.objects.filter(tv_type=film_type, title__icontains=finder)
        return {'all_tv': filtered}


def films(request):
    if (context := filter_films(request, 'f')):
        return render(request, 'tv/tv.html', context)
    films_titles = Tv.objects.filter(tv_type='f')
    return render(request, 'tv/tv.html', {'all_tv': films_titles})


def series(request):
    if (context := filter_films(request, 's')):
        return render(request, 'tv/tv.html', context)
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
