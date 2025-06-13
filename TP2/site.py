from flask import Flask, request, render_template
import json
import re
app = Flask(__name__)


db_file = open("json_completo.json", encoding="utf-8")

db = json.load(db_file)
db_file.close()

@app.route("/")
def homepage():
    return render_template("home.html")

'''
dados_filtrados = []
for dic in db:
    dicionario = {}
    for chave in dic:
        dicionario[chave] = dic[chave]

    dados_filtrados.append(dicionario)
'''
@app.get("/conceitos/")
def conceitos_tabela():

    return render_template("conceitos_tabela.html", conceitos=db)


@app.get("/conceitos/<designacao>")
def conceito(designacao):
    for item in db:
        if item.get("conceito").lower() == designacao.lower():
            return render_template("conceito.html", conceito=item)

    return render_template("conceito.html", conceito={"conceito": "Erro", "descricao": "Conceito não encontrado"})


app.run(host="localhost", port=4002, debug=True)
