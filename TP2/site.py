from flask import Flask, request, render_template
from markupsafe import Markup
import copy
import html
import json
import re

app = Flask(__name__)


db_file = open("json_completo.json", encoding="utf-8")

db = json.load(db_file)
db_file.close()



'''
dados_filtrados = []
for dic in db:
    dicionario = {}
    for chave in dic:
        dicionario[chave] = dic[chave]

    dados_filtrados.append(dicionario)
'''


associacoes_dic = {}



#dicionario de associacoes
for conceito in db:
    for key, value in conceito.items():
        match = re.match(r"outras associacoes a '(.*)'", key)
        if match:
            termo = match.group(1)
            associacoes_dic[termo] = value



#print(associacoes_dic)


#lista de areas medicas unicas
areas_medicas=[]
for conceito in db:
    if "área médica" in conceito:
        areas_medicas.append(conceito["área médica"])


areas_medicas =list(set(areas_medicas))


def aplicar_tooltips(texto, associacoes_dict):
    for palavra, associacoes in associacoes_dict.items():
        tooltip_raw = "<br>".join(associacoes) #br é tipo um enter
        tooltip_escaped = html.escape(tooltip_raw) #dá escape a caracteres especiais

        padrao = r'(?<!["=])\b(' + re.escape(palavra) + r')\b(?![^<]*?>)' #garantir que nao estou a mexer nas outras tags da pagina html
        substituto = (
            r'<span data-bs-toggle="tooltip" data-bs-html="true" '
            f'title="{tooltip_escaped}" '
            r'style="border-bottom: 1px dotted #000;">\1</span>'
        )

        texto = re.sub(padrao, substituto, texto, flags=re.IGNORECASE)

    return Markup(texto)

@app.route("/")
def homepage():
    return render_template("home.html")



@app.get("/conceitos/")
def conceitos_tabela():

    return render_template("conceitos_tabela.html", conceitos=db)


@app.get("/conceitos/<designacao>")
def conceito(designacao):
    for item in db:
        if item.get("conceito").lower() == designacao.lower():

            # para não modificar o original (inicialmente depois de entrar num conceito ele aplicava essas tooltips ja carregadas nas outras paginas)
            item_copy = copy.deepcopy(item)

            campos_de_texto = [
                "contexto",
                "significado",
                "significado_enciclopédico",
                "definicao catalã"
            ]

            for campo in campos_de_texto:
                if campo in item_copy:
                    item_copy[campo] = aplicar_tooltips(item_copy[campo], associacoes_dic)

            return render_template("conceito.html", conceito=item_copy)

    return render_template("conceito.html", conceito={"conceito": "Erro", "descricao": "Conceito não encontrado"})



@app.route("/areas")
def pag_areas():
    return render_template("areas.html", areas=areas_medicas)


@app.get("/areas/<area>")
def area_especifica(area):

    conceitos_area=[]

    for item in db:

        if not item.get("área médica"):
            continue
        elif item.get("área médica").lower() == area.lower():

            conceitos_area.append(item)



    return render_template("tabela_area_conceitos.html", conceitos=conceitos_area , area=area)





app.run(host="localhost", port=4002, debug=True)


