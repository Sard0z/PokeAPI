from urllib.request import urlopen

from django.shortcuts import render
from django.http import HttpResponse
from .forms import PokemonSearchForm
from PIL import Image
import requests

# Create your views here.


def search_pokemon(request):
    if request.method == 'POST':
        form = PokemonSearchForm(request.POST)
        if form.is_valid():
            pokemon_name_or_id = form.cleaned_data['pokemon_name_or_id']
            return get_pokemon_info(request, pokemon_name_or_id)

    form = PokemonSearchForm()

    return render(request, 'search_pokemon.html', {'form': form})


def get_pokemon_info(request, pokemon_name_or_id):
    api_url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name_or_id.lower()}/"
    response = requests.get(api_url)

    if response.status_code == 200:
        pokemon_data = response.json()
        image_url = pokemon_data['sprites']['other']['official-artwork']['front_default']
        Image.open(urlopen(image_url))
        return render(request, 'pokemon_info.html', {'pokemon_data': pokemon_data, 'image_url': image_url})

    return HttpResponse(f"Error {response.status_code}: No se pudo obtener información del Pokemon")
