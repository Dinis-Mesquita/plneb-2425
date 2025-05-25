from bs4 import BeautifulSoup
import requests
import json


response= requests.get("https://www.atlasdasaude.pt/doencasAaZ")
html_content = response.text
soup = BeautifulSoup(html_content,'html.parser')

var = soup.find_all("div",class_="views-row")

'''
for linha in var:
    texto=linha.get_text()
    a=texto.split(" \n  ")

    conceito=a[0].strip("\n")
    definicao=a[1].strip("\n")
    print(f"{conceito} \n {definicao} \n \n")
    '''


doencas = {}
for div_row in soup.find_all("div", class_="views-row"):
    designacao = div_row.div.h3.a.text
    #print(designacao)
    desc_div = div_row.find("div", class_="views-field-body")
    if desc_div.div.p:
        desc = desc_div.div.p.text

    elif desc_div.div.div:
        desc = desc_div.div.div.text

    doencas[designacao] = desc

print(doencas)

f_out = open("doencas.json", "w" ,encoding= "utf8")

json.dump(doencas, f_out, indent = 4,ensure_ascii = False)

f_out.close()


