from django.urls import path

from . import views

app_name = 'core'

urlpatterns = [
    path('movie/<int:pk>',
         views.MovieDetail.as_view(),
         name='MovieDetail'),

    path('movies',
         views.MovieList.as_view(),
         name='MovieList'),

    path('person/<int:pk>',
         views.PersonDetail.as_view(),
         name='PersonDetail'),

    path('persons',
         views.PersonList.as_view(),
         name='PersonList'),

    ]