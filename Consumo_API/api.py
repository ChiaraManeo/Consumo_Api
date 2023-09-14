import requests

# URL da API que você deseja consultar
url = "https://api.kanye.rest"

# Fazendo uma solicitação GET
response = requests.get(url)

# Verificando se a solicitação foi bem-sucedida (código de status 200)
if response.status_code == 200:
    # Imprimindo os dados da resposta (geralmente em formato JSON)
    frase = response.json()
    print(frase)
        
else:
    print("Erro na solicitação:", response.status_code)
    
    {

}