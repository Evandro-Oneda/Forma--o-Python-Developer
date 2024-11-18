import re 
import json
from urllib.request import urlopen

url = "https://ipinfo.io/json"

resposta = urlopen(url)

dados = json.load(resposta)

#print(dados)

ip = dados["ip"]
org = dados["org"]
cidade = dados["city"]
pais = dados["country"]
regiao = dados["region"]


print("DADOS:")
print(f"IP: {ip} \nOrganizacao: {org}  \nPais: {pais} \nRegiao: {regiao}\nCidade: {cidade}")