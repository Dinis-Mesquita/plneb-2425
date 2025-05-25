import spacy
import sys

nlp = spacy.load("pt_core_news_lg")  # make sure to use larger package!
nlp.add_pipe("merge_entities")
doc1 = nlp("O Manel gosta de papas de sarrabulho e francesinhas. Faz ele muito bem.")


def main(text):
    f = nlp(text)
    n = 1
    for frase in f.sents:
        print(f"# {n}")
        for p in frase:
            if p.pos_ != "SPACE":
                print(p.text, "|", p.pos_, "|", p.ent_type_)
            else:
                print(p.text, "|", p.pos_, "|", p.lemma_)

            n += 1


# file = sys.argv[1]
# with open (file) as f:
#    text = f.read()
main(doc1)