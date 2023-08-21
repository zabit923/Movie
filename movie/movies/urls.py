from django.urls import path

from . import views




urlpatterns = [
    path('', views.MovieView.as_view(), name='index'),
    path('filter/', views.FilterMoviesView.as_view(), name='filter'),
    path('<slug:slug>/', views.MovieDetailViews.as_view(), name='movie_detail'),
    path('review/<int:pk>/', views.AddReview.as_view(), name='add_review'),
    path('actor/<str:slug>/', views.ActorView.as_view(), name='actor_detail')
]
