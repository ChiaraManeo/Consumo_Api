import requests

url = "https://api.chucknorris.io/jokes/random"

response = requests.get(url)

if response.status_code == 200:
    fatos = response.json()
    for chuck in fatos['categories']:
        print('Fatos sobre Chuck:', chuck['value'])
else:
    print("Erro na solicitação:", response.status_code)
    
    {

}