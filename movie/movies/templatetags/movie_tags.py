from django.apps import apps
from django import template




register = template.Library()

@register.simple_tag()
def get_categories():
    Category = apps.get_model('movies', 'Category')
    return Category.objects.all()

@register.inclusion_tag('movies/tags/last_movie.html')
def get_last_movies(count=5):
    Movie = apps.get_model('movies', 'Movie')
    movies = Movie.objects.order_by('id')[:count]
    return {'last_movies': movies}


