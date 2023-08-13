from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from movie.Common.views import TitleMixin




class MovieView(TitleMixin, ListView):
    model = Movie
    queryset = Movie.objects.filter(draft=False)
    template_name = 'movies/movie_list.html'
    title = 'Movies'


class MovieDetailViews(TitleMixin, DetailView):
    model = Movie
    slug_field = 'url'
    template_name = 'movies/movie_detail.html'
    title = 'MovieDetails'



