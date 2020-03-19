from django.contrib import admin
from .models import *


# Register your models here.
# admin.site.register(Movie)
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['title', 'description']
    list_display = ['title', 'year', 'imdb']
    search_fields = ['title', 'description']
    list_filter = ['year', 'imdb']

admin.site.register(Actor)
admin.site.register(Director)
admin.site.register(Comment)
