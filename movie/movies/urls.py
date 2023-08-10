from django.urls import path

from . import views




urlpatterns = [
    path('', views.MovieView.as_view()),
    path('<int:pk>/', views.MovieDetailViews.as_view())
]
