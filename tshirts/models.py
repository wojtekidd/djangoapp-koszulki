from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User
from taggit.managers import TaggableManager


# Create your models here.
class Tshirt(models.Model):
    Sizes = (
        ('XXS', 'XXS'),
        ('XS', 'XS'),
        ('S', 'S'),
        ('M', 'M'),
        ('L', 'L'),
        ('XL', 'XL'),
        ('XXL', 'XXL'),
    )
    brand = models.CharField(max_length=256, verbose_name='Brand name', help_text='')
    design = models.CharField(max_length=256, verbose_name='Design name', help_text='')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    size = models.CharField(choices=Sizes, max_length=3, default='M')
    video = models.FileField(upload_to='videos/', default='', blank=True, help_text='')
    image = models.ImageField(upload_to='pics/', default='', help_text='')

    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)

    tags = TaggableManager()



# TODO: Add image and video size limits, add tags, colors, supplier class, ForeignKey relation? Brand has to become another Class!


    def __str__(self):
        return f'{self.design} - {self.brand} - created {self.created}'


    class Meta:
        verbose_name = 'T-shirt'
        verbose_name_plural = 'T-shirts'
        '''ordering = ['title', '-pubdate']'''


class Story(models.Model):
    story = models.TextField(max_length=400, help_text='')  # changed atr name to story
    stars = models.IntegerField(default=5,
                                    validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Story'
        verbose_name_plural = 'Stories'
        '''ordering = ['title', '-pubdate']'''

    def __str__(self):
        return f"Story of {self.tshirt}"

