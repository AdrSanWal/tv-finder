from django.urls import path

from . import views

urlpatterns = [
    path('<filter_type>/', views.films, name='films'),
    path('<filter_type>/<int:filter_id>/', views.filtered_film, name='filtered_film'),
]
