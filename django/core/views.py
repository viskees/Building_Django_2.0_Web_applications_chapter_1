from django.shortcuts import render
from django.views.generic import ListView, DetailView
from core.models import Movie

# Create your views here.

class MovieDetail(DetailView):
    model = Movie

class MovieList(ListView):
    model = Movie
    paginate_by = 5