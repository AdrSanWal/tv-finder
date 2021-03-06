from django.urls import path

from . import views

urlpatterns = [
    path('<film_type>/', views.films, name='films'),
    path('<film_type>/<int:filter_id>/', views.filtered_film, name='filtered_film'),
]
