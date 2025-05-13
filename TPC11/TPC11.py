import time

from bs4 import BeautifulSoup
import requests
import json

#keywords, abstract, titulo, DOI, data
def artigo(url_artigo):


        response = requests.get(url_artigo)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        titulo = soup.find("article", class_="obj_article_details").h1.text.strip()

        data = soup.find("div", class_="item published").section.div.text.strip()

        abstract = soup.find("section", class_="item abstract")
        abs_list = abstract.find_all("p")
        try:
            introducao =abs_list[0].text.strip()
            metodos = abs_list[1].text.strip()
            resultados = abs_list[2].text.strip()
            conclusao = abs_list[3].text.strip()
        except :
            introducao = ""
            metodos = ""
            resultados = ""
            conclusao = ""

        try:
            doi = (soup.find("section", class_="item doi").span.a).get('href')

        except:
            doi=""
        try:
            keywords = (soup.find("section", class_="item keywords").span.text.strip()).replace("\t","")
        except:
            keywords = ""



        dic = {
            "url": url_artigo,
            "titulo": titulo,
            "keywords": keywords,
            "introducao": introducao,
            "metodos": metodos,
            "resultados": resultados,
            "conclusao": conclusao,
            "doi": doi,
            "data": data
        }
        return dic




def issues(url_issue):
    try:
        response = requests.get(url_issue)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')

        lista_artigos = soup.find("h2",  string=lambda t: t.strip() == 'Original Articles')
        lista_artigos=lista_artigos.find_next_sibling('ul', class_='cmp_article_list articles')
        lista_artigos=lista_artigos.find_all("li",recursive=False)
        links=[]

        for artigo in lista_artigos:
            link = artigo.find("h3",class_="title").a.get('href')

            links.append(link)

        return links

    except:
        links=[]
        return links



def fvolumes(url_volume):


        response = requests.get(url_volume)
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        lista_volumes = soup.find("ul",class_="issues_archive")
        lista_volumes=lista_volumes.find_all("li",recursive=False)
        volumes=[]
        for volume in lista_volumes:
            link = volume.a.get("href")
            volumes.append(link)

        return volumes


json_final=[]
for i in range(1,7):
    url = f"https://revista.spmi.pt/index.php/rpmi/issue/archive/{i}"

    print(f"{url}\n\n")
    volumes = fvolumes(url)
    links_artigos=[]
    for volume in volumes:
        artigos=issues(volume)
        print(volume)

        #print(artigos)

        for link in artigos:
            print(artigo(link))
            json_final.append(artigo(link))


f_out = open("tpc11.json", "w", encoding="utf-8")

json.dump(json_final, f_out, indent=4, ensure_ascii=False)
