
import requests
from django.shortcuts import render

def country_list(request):
    url = 'https://api.worldbank.org/v2/countries?format=json'
    response = requests.get(url)
    data = response.json()[1]
    countries = []
    for country in data:
        countries.append({
            'name': country['name'],
            'iso2code': country['iso2Code']
        })
    context = {'countries': countries}
    return render(request, 'myapp/country_list.html', context)



def country_detail(request, iso2code):
    url = f'https://api.worldbank.org/v2/country/{iso2code}/indicator/SP.POP.TOTL?format=json'
    response = requests.get(url)
    data = response.json()[1]
    population_data = []
    for entry in data:
        if entry['value'] is not None:
            population_data.append({
                'year': entry['date'],
                'population': entry['value']
            })
    context = {'population_data': population_data, 'country_name': data[0]['country']['value']}
    return render(request, 'myapp/country_detail.html', context)
