from django.shortcuts import render, redirect
from django.views.decorators.http import require_safe
from django.contrib.auth.decorators import login_required
from .models import Genre, Movie
from django.http import JsonResponse

# Create your views here.
@require_safe
def index(request):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    context = {
        'movies': movies,
        'genres': genres,
    }

    return render(request, 'movies/index.html', context)


@require_safe
def detail(request, movie_pk):
    movie = Movie.objects.get(pk=movie_pk)
    context = {
        'movie':movie,
    }
    return render(request, 'movies/detail.html', context)


@require_safe
def recommended(request, genre_pk):
    movies = Movie.objects.all()
    genres = Genre.objects.all()

    movie_lst = []
    for movie in movies:
        m = movie.genres.values()
        # print(m)
        # lst.append(movie.title)
        # lst.append(movie.vote_average)
        for i in m:
            if i['id'] == genre_pk:
                movie_lst .append(movie)


    #     movie_lst.append(lst)
    # # print(movie_lst)
    # movielst = []
    # for mo in movie_lst:
    #     if genre_pk in mo:
    #         movielst.append(m[0])
    # movielst.sort(key=lambda x:x[1], reverse=True)



    context = {
        'movies': movies,
        'genres': genres,
        'genre_pk':genre_pk, 
        'movie_lst':movie_lst,
        
    }
    return render(request, 'movies/recommended.html', context)