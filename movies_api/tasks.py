
from celery import shared_task
from .models import Movies

@shared_task
def update_movie_ranks():
    # Get movies that need rank updates (coming-up, starting, running)
    movies_to_update = Movies.objects.filter(status__in=['coming-up', 'starting', 'running'])

    for movie in movies_to_update:
        movie.rank += 10
        movie.save()
       