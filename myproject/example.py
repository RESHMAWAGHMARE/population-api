import requests

def get_population_data(iso2Code):
    url = f'https://api.worldbank.org/v2/country/{iso2Code}/indicator/SP.POP.TOTL?format=json'
    response = requests.get(url)
    data = response.json()[1]
    population = []
    for year in data:
        population.append({
            'year': year['date'],
            'value': year['value'],
        })
    return population
population_data = get_population_data('US')
print(population_data)
