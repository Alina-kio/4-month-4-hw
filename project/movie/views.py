from django.shortcuts import render
from .models import Director, Movie, Review
# Create your views here.

def movie_list_view(request):
    context = {
        'movie_list': Movie.objects.all(),
        'director_list': Director.objects.all()
    }
    return render(request, "movie.html", context=context)


def movie_detail_view(request, id):
    # movies = Movie.objects.prefetch_related('rewiews').get(id=id)
    movies = Movie.objects.get(id=id)
    context = {
        'movie_detail': movies,
        'reviews': Review.objects.filter(movie=movies)
    }
    return render(request, 'detail.html', context=context)