from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=30)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.gender}'


class Director(models.Model):
    name = models.CharField(max_length=30)
    birth = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.birth}'


class Tv(models.Model):
    tv_type = models.CharField(max_length=5, choices=[('s', 'serie'), ('f', 'film')])
    title = models.CharField(max_length=50, unique=True,)
    original_title = models.CharField(max_length=50, blank=True, null=True)
    seasons = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='tvfinder', null=True, blank=True)
    gender = models.ManyToManyField(Gender)
    year = models.IntegerField()
    director = models.ManyToManyField(Director)
    country = models.CharField(max_length=30, blank=True, null=True)
    rating = models.FloatField()
    summary = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.title}, {self.gender}, {self.year}, {self.rating}'
