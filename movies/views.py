from django.shortcuts import render
from django.http import JsonResponse
from django.core import serializers
from .models import Movie
from .apis import fetch_movies


def index(request):
    movies = Movie.objects.all()
    context = {'movies': movies}
    return render(request, 'movies/index.html', context)


def update_db(request):
    movies = fetch_movies()
    new_movies = []
    for movie in movies:
        movie_code = movie.get('movieCd')
        if not Movie.objects.filter(code=movie_code).exists():
            new_movie = Movie.objects.create(code=movie_code, title=movie.get('movieNm'))
            new_movies.append(movie)
    return JsonResponse(new_movies, safe=False)
