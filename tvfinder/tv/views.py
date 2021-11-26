from django.shortcuts import render

from .models import Tv, Director, Gender


def films(request, filter_type):
    finder = request.GET.get('finder')
    if finder != '' and finder is not None:
        filtered = Tv.objects.filter(tv_type=filter_type, title__icontains=finder)
        context = {'all_tv': filtered}
    else:
        all_tv = Tv.objects.filter(tv_type=filter_type)
        context = {'all_tv': all_tv}
    return render(request, 'tv/tv.html', context)


def filtered_film(request, filter_type, filter_id):
    filtered_film = Tv.objects.get(id=filter_id)
    filter_type = filtered_film.tv_type
    directors = Director.objects.filter(directors__in=[filter_id])
    genders = Gender.objects.filter(genders__in=[filter_id])
    return render(request, 'tv/film.html', {'filtered_film': filtered_film,
                                            'genders': genders,
                                            'directors': directors})
