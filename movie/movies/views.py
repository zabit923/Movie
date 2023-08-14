from django.shortcuts import render, redirect
from django.views.generic import ListView, DetailView
from django.views.generic.base import View

from .models import Movie
from movie.Common.views import TitleMixin
from .forms import ReviewForm




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


class AddReview(View):
    def post(self, request, pk):
        form = ReviewForm(request.POST)
        movie = Movie.objects.get(id=pk)
        if form.is_valid():
            form = form.save(commit=False)
            form.movie = movie
            form.save()
        return redirect(movie.get_absolute_url())
