import requests

url = "https://api.kanye.rest/"

response = requests.get(url)

if response.status_code == 200:
    
    data = response.json()
    frase = data['quote']
    print("Frase de Kanye West:", frase)
else:
    print("Erro na solicitação:", response.status_code)
