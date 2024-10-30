from bs4 import BeautifulSoup

import requests

#site recebe todo conteudo da requisiçao http

site = requests.get("https://www.climatempo.com.br/previsao-do-tempo/cidade/558/saopaulo-sp/").content

#soup baixa todo conteudo do site html

soup = BeautifulSoup(site, "html.parser")

# print transforma o html em string
#print(soup.prettify())

localidade = soup.find({"h1", "class_=""-bold" "-font-18 -dark-blue _margin-r-10 _margin-b-sm-5"}).text

temperatura_minima = soup.find("span", class_="-gray-light", id="min-temp-1")
temperatura_maxima = soup.find("span", class_="-gray-light", id="max-temp-1")

localidade_formatado = localidade.replace("\n", " ")
print(localidade_formatado.replace("\t", ""))

print("temperatura minima: ", temperatura_minima.string)

print("temperatura maxima: ",temperatura_maxima.string)
