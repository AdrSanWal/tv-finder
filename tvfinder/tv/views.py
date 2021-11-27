from django.shortcuts import render

from .models import Tv, Director, Gender


def get_values(films):
    years = [film.year for film in films]
    countries = set([film.country for film in films])
    films_ids = [film.id for film in films]
    genders = set(Gender.objects.filter(genders__in=films_ids))
    return {'min_year': min(years),
            'max_year': max(years),
            'countries': countries,
            'films_ids': films_ids,
            'genders': genders}


def films(request, film_type):
    finder = request.GET.get('finder')
    if finder != '' and finder is not None:
        films = Tv.objects.filter(tv_type=film_type, title__icontains=finder)
    else:
        films = Tv.objects.filter(tv_type=film_type)
    context = get_values(films)

    return render(request, 'tv/tv.html', {'all_tv': films,
                                          'film_type': film_type,
                                          **context})


def sidebar_filter(request, film_type, filter_type, value):
    if filter_type == 'country':
        films = Tv.objects.filter(tv_type=film_type, country=value)
        context = get_values(films)
    if filter_type == 'gender':
        gender_id = Gender.objects.get(gender=value)
        films = Tv.objects.filter(tv_type=film_type, gender=gender_id.id)
        context = get_values(films)
    return render(request, 'tv/tv.html', {'all_tv': films,
                                          'film_type': film_type,
                                          **context})


def filtered_film(request, film_type, filter_id):
    filtered_film = Tv.objects.get(id=filter_id)
    film_type = filtered_film.tv_type
    directors = Director.objects.filter(directors__in=[filter_id])
    genders = Gender.objects.filter(genders__in=[filter_id])
    return render(request, 'tv/film.html', {'filtered_film': filtered_film,
                                            'genders': genders,
                                            'directors': directors})
