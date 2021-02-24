from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import *

# Create your views here.

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    model = Movie
    paginate_by = 5

class PersonDetail(DetailView):
    queryset = Person.objects.all_with_prefetch_movies()

class PersonList(ListView):
    model = Person
    paginate_by = 5
