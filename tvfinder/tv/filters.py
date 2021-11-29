from django.db.models.query_utils import FilteredRelation
from django_filters import FilterSet
from .models import Tv, Gender, Director


class TvFilter(FilterSet):
    class Meta:
        model = Tv
        fields = {
            'title': ['icontains'],
            'year': ['gte', 'lte'],
            'rating': ['gte', 'lte'],
            'country': ['iexact'],
        }


class GenderFilter(FilterSet):
    class Meta:
        model = Gender
        fields = {
            'id': ['exact'],
            'gender': ['exact']
        }
