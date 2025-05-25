from bs4 import BeautifulSoup
import requests
import json


'''
for linha in var:
    texto=linha.get_text()
    a=texto.split(" \n  ")

    conceito=a[0].strip("\n")
    definicao=a[1].strip("\n")
    print(f"{conceito} \n {definicao} \n \n")
    '''


def doencas_letra(letra):
    url="https://www.atlasdasaude.pt/doencasaaz/" + letra
    print(url)
    response= requests.get(url)

    html_content = response.text
    soup = BeautifulSoup(html_content,'html.parser')

    var = soup.find_all("div",class_="views-row")



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

    return doencas

res={}
for a in range(97, 123):
    letra = chr(a)
    doencas_letra(letra)
    res = res | doencas_letra(letra)


f_out = open("doencas_.json", "w" ,encoding= "utf8")

json.dump(res, f_out, indent = 4,ensure_ascii = False)

f_out.close()


