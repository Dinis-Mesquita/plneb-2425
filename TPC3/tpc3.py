import re


file = open("dicionario_medico.txt", encoding="utf-8")

texto= file.read()

#limpeza

texto= re.sub(r"\n\f","", texto)  #tpc3


#marcar
texto= re.sub(r"\n\n","\n\n@", texto)

def limpa_descicao(descricao):
    descricao = descricao.strip()
    descricao =re.sub(r"\n"," ", descricao)
    return descricao


#extrair conceitos
conceitos = re.findall(r"@(.*)\n([^@]*)",texto)


result = [(designacao, limpa_descicao(descricao)) for designacao, descricao in conceitos]


#print(result)

def gera_html(result):
    html_header = f"""
                <!DOCTYPE html>
                    <head>
                    <meta charset="UTF-8"/>
                    </head>

                    <body>
                    <h3>Dicionario de conceitos médicos</h3>
                    <p>Este dicionario foi desenvolvido para a aula de PLNEB 2024/2025<p>
                        
                        """
    html_conceitos=""
    for designacao, descricao in result:
        html_conceitos += f"""
            <div>
            <p><b>{designacao}</b></p>
            <p>{descricao}</p>
            </div>
            <hr/>
            """



    html_footer ="""
                </body>
                </html>
                
            """
    return html_header+html_conceitos+html_footer

html=gera_html(result)

f_out = open("dicionario_medico.html","w", encoding="utf-8")
f_out.write(html)
file.close()