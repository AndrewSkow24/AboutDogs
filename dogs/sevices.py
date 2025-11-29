from config.settings import CACHE_ENABLED
from dogs.models import Dog
from django.core.cache import cache


def get_dogs_from_cache():
    if not CACHE_ENABLED:
        return Dog.objects.all()
    key = "dog_list"
    dogs = cache.get(key)
    if dogs is not None:
        return dogs
    else:
        dogs = Dog.objects.all()
        cache.set(key, dogs)

    return dogs
