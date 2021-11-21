from django.urls import path

from . import views

urlpatterns = [
    path('f/', views.films, name='films'),
    path('s/', views.series, name='series'),
    path('<filter_type>/<int:filter_id>/', views.filtered_film, name='filtered_film'),
]
