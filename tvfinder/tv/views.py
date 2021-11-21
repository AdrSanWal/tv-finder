from django.shortcuts import render


def films(request):
    text = 'Peliculas'
    return render(request, 'tv/tv.html', {'text': text})


def series(request):
    text = 'Series'
    return render(request, 'tv/tv.html', {'text': text})
