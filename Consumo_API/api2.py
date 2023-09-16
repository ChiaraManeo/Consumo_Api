import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    frase = data['value']
    print('Fatos sobre Chuck:', frase)

else:
    print("Erro na solicitação:", response.status_code)
