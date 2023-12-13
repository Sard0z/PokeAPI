from django import forms


class PokemonSearchForm(forms.Form):
    pokemon_name_or_id = forms.CharField(label='Nombe o ID del pokemon', max_length=100)
