import re
import json

file = open('dicionario_medico.xml', "r", encoding = 'utf8')
texto = file.read()
file.close()

# LIMPEZA
# Apagar page
texto = re.sub(r"</?page.*?>", "", texto)

# Apagar text
texto = re.sub(r"</?text.*?>", "", texto) #ponto de interrogação torna o quantificador lazy- natrualmente, asterisco é greedy


# EXTRAIR
conceitos = re.findall(r"<b>(.)</b>\n([^<])", texto)

def limpa_descricao(desc):
    desc = desc.strip()
    desc = re.sub(r"\n", "", desc)
    return desc

#conceitos_dict = {designacao : limpa_descricao(descricao) for  designacao, descricao in conceitos}
conceitos_dict = {}
for designacao, descricao in conceitos:
    descricao = limpa_descricao(descricao)
    if designacao in conceitos_dict:
        conceitos_dict[designacao] += " @ " + descricao
    else:
        conceitos_dict[designacao] = descricao

#print(conceitos_dict)


#Criar ficheiro JSON

file_out = open('conceitos.json', 'w', encoding = 'utf8')
json.dump(conceitos_dict, file_out, ensure_ascii=False, indent = 4)
file_out.close()