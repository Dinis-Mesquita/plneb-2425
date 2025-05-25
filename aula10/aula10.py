from gensim.models import Word2Vec
from gensim.utils import tokenize
import gensim
f1= open (r"C:\Users\dinis\Desktop\pln\aula10\Harry_Potter_Camara_Secreta-br.txt","r",encoding="utf8")
f2= open(r"C:\Users\dinis\Desktop\pln\aula10\Harry_Potter_e_A_Pedra_Filosofal.txt","r",encoding="utf8")

# tokenizar cada frase em palavras
sents=[]
for frase in f1:
    tokens = list(gensim.utils.tokenize(frase,lower=True))
    sents.append(tokens)

for frase in f2:
    tokens = list(gensim.utils.tokenize(frase,lower=True))
    sents.append(tokens)

#print(sents)


model=Word2Vec(sents,vector_size=300,epochs=20)

print(model.wv.doesnt_match(["harry","varinha","dumbledore"]))
#print(model.wv["harry"])
#print(model.wv.most_similar('harry'))
print(model.wv.most_similar(positive=["bruxo","dursley"],negative=["magia"]))  # +king - man + woman =queen
#print(model.wv.similarity('harry','hagrid'))
#print(model.wv.similarity('harry','dobby'))
f1.close()
f2.close()

model.wv.save_word2vec_format("mode_harry.txt",binary=False)

#python -m gensim.scripts.word2vec2tensor -i mode_harry.txt -o model_harry
#https://projector.tensorflow.org