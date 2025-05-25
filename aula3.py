import re


file = open("dicionario_medico.txt", encoding="utf-8")

texto= file.read()

#limpeza

texto= re.sub(r"\f","", texto)

#linha130
#marcar
texto= re.sub(r"\n\n","\n\n@", texto)

conceitos_texto =re.split(r"\n\n@",texto)

conceitos_list=[]
for c in conceitos_texto:
    conceito_raw=  re.split(r"\n",c, maxsplit=1)
    if len(conceito_raw)>1:
        conceito, designacao = conceito_raw
        descricao = re.sub(r"\n", " ", designacao)
        conceitos_list.append(conceito,descricao)

print(conceitos_list)
file.close()