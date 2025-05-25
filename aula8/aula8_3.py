from bs4 import BeautifulSoup
import requests
import json

def doencas_letra(letra):
    url="https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response= requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content,'html.parser')

    var = soup.find_all("div",class_="views-row")
node_doencas
for elem in var:
    refs=elem.a
    ref=refs.get("href")
    url="https://www.atlasdasaude.pt" + ref

    respostas = requests.get(url)
    html_conteudo = response.text
    sopa = BeautifulSoup(html_content, 'html.parser')

    print(refs)