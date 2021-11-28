from django.db import models


class Gender(models.Model):
    gender = models.CharField(max_length=30, unique=True,)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["gender"]
        verbose_name = "Gender"
        verbose_name_plural = "Genders"

    def __str__(self):
        return f'{self.gender}'


class Director(models.Model):
    name = models.CharField(max_length=30, unique=True,)
    birth = models.IntegerField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "Director"
        verbose_name_plural = "Directors"

    def __str__(self):
        return f'{self.name}, {self.birth}'


class Tv(models.Model):
    tv_type = models.CharField(max_length=5, choices=[('s', 'serie'), ('f', 'film')])
    title = models.CharField(max_length=80, unique=True,)
    original_title = models.CharField(max_length=80, blank=True, null=True)
    seasons = models.IntegerField(blank=True, null=True)
    photo = models.ImageField(upload_to='tvfinder', null=True, blank=True)
    gender = models.ManyToManyField(Gender, related_name='genders')
    year = models.IntegerField()
    director = models.ManyToManyField(Director, related_name='directors')
    country = models.CharField(max_length=30, blank=True, null=True)
    rating = models.FloatField()
    summary = models.TextField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]
        verbose_name = "Film"
        verbose_name_plural = "Films"
        
    def __str__(self):
        return f'{self.title}, {self.gender}, {self.year}, {self.rating}'
