from django_filters import FilterSet
from .models import Tv, Gender, Director


class TvFilter(FilterSet):
    class Meta:
        model = Tv
        fields = {
            'year': ['gte', 'lte'],
            'rating': ['gte', 'lte'],
            'country': ['exact'],
            'gender': ['exact'],
        }
