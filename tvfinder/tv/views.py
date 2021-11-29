from django.shortcuts import render

from .filters import TvFilter
from .models import Tv, Director, Gender


def films(request, film_type):
    queryset = Tv.objects.filter(tv_type=film_type).prefetch_related('gender')
    films = TvFilter(request.GET, queryset=queryset)

    films_ids = films.qs.values('id')
    genders = Gender.objects.filter(rel_genders__in=films_ids).distinct()

    years = [film.year for film in films.qs]
    min_year = min(years) if years else None
    max_year = max(years) if years else None

    countries = set([film.country for film in films.qs])

    return render(request, 'tv/tv.html', {'films': films,
                                          'film_type': film_type,
                                          'min_year': min_year,
                                          'max_year': max_year,
                                          'countries': countries,
                                          'genders': genders,
                                          })


def filtered_film(request, film_type, filter_id):
    filtered_film = Tv.objects.get(id=filter_id)
    film_type = filtered_film.tv_type
    directors = Director.objects.filter(rel_directors__in=[filter_id])
    genders = Gender.objects.filter(rel_genders__in=[filter_id])
    return render(request, 'tv/film.html', {'filtered_film': filtered_film,
                                            'genders': genders,
                                            'directors': directors})
