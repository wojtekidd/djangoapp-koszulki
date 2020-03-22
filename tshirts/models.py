from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


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

    brand = models.CharField(max_length=256, verbose_name='Brand name')
    design = models.CharField(max_length=256, verbose_name='Design name')
    created = models.DateTimeField(auto_now_add=True, editable=False)
    size = models.CharField(choices=Sizes, max_length=3, default='M')
    # image =
    # video =


    def __str__(self):
        return f'{self.design} - {self.brand} - created {self.created}'


    class Meta:
        verbose_name = 'T-shirt'
        verbose_name_plural = 'T-shirts'

class Story(models.Model):
    body = models.TextField(max_length=400)
    stars = models.IntegerField(default=5,
                                    validators=[MinValueValidator(1), MaxValueValidator(5)])
    created = models.DateTimeField(auto_now_add=True)
    tshirt = models.ForeignKey('Tshirt', on_delete=models.CASCADE)
