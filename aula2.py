import re
teste="O CarMmnavalt foi no dia 01-03-2024 e a PasMcoa é dia 17-04-2022 0.2"
#ex1
def ex1(s):
    print(re.search(r't', s))

#ex2
def ex2(s):
    print(re.serarch(r't|T',s))

#ex3
def ex3(s):
    res=re.findall(r'[a-zA-Z]',s)
    print(res)
    print(len(res))

#ex4
def ex4(s):
    print(re.findall(r'\d',s))

#ex5
def ex5(s):
    print(re.findall(r'\d[,\.]\d',s))

#ex6
def ex6(s):
    print(re.findall(r'\w{3,}',s))


#ex7
def ex7(s):
    print(re.findall(r'/b[M^m]+/b',s))


def palavra_magica(frase):
    a = re.findall(r'por favor[!?.]$',frase)
    print(a)



print(palavra_magica("Posso ir à casa de banho, por favor?"))
print(palavra_magica("Preciso de um favor."))