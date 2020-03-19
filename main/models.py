from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


# Create your models here.
class Movie(models.Model):
    MPAA = (
        ('-', 'None'),
        ('G', 'G rating'),
        ('PG-13', 'PG-13 rating'),
        ('NC-17', 'NC-17 rating')
    )

    title = models.CharField(max_length=256, verbose_name='Full title')
    description = models.TextField(default='')
    year = models.IntegerField(null=True, blank=True)
    released = models.DateField(null=True, blank=True)
    imdb = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    poster = models.ImageField(null=True, blank=True)
    trailer_video = models.URLField(null=True, blank=True)
    #adding timestamp
    created = models.DateTimeField(auto_now_add=True, editable=False)
    mpaa_rating = models.CharField(choices=MPAA, max_length=5, default='G')
    #add rating
    actors = models.ManyToManyField("Actor", related_name="movies")


    def __str__(self):
        return f'{self.title} - {self.year}'


    class Meta:
        verbose_name = "Movie"
        verbose_name_plural = "Movies"


class Actor(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "actor"
        verbose_name_plural = "actors"


class Director(models.Model):
    first_name = models.CharField(max_length=100, null=False)
    last_name = models.CharField(max_length=100, null=False)
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    class Meta:
        verbose_name = "director"
        verbose_name_plural = "directors"

class Comment(models.Model):
    body = models.TextField(max_length=400)
    stars = models.IntegerField(default=5,
                                validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    movie = models.ForeignKey('Movie', on_delete=models.CASCADE)
