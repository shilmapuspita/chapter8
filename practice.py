import requests

api_key = '66cab81b-51d0-4df6-82bd-82a95ebff787'
word = 'voluminous'
root_url = 'https://www.dictionaryapi.com/api/v3/references/collegiate/json'
final_url = f'{root_url}/{word}?key={api_key}'
r = requests.get(final_url)
result = r.json()

for result in result:
    print(result) 