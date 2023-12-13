from django.urls import path
from .views import get_pokemon_info, search_pokemon

urlpatterns = [
    path('search/', search_pokemon, name='search_pokemon'),
    path('pokemon_info/<str:pokemon_name_or_id>/', get_pokemon_info, name='pokemon_info'),
]
