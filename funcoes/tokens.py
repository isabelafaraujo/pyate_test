import spacy

def custom_sentencizer(doc):
    for i, token in enumerate(doc[:-2]):
        if token.text == "\n" and doc[i+1].is_title:
            doc[i+1].is_sent_start = True
        else:
            doc[i+1].is_sent_start = False
    return doc

###
vocab = nlp.vocab
sample_text = "Frase de exemplo (a)"
nlp.tokenizer.explain(sample_text)

###
nlp.tokenizer.explain(string)

###
def print_tokens(text):
    a_r = []
    doc = nlp(text)
    spacy_frame = pd.DataFrame(columns = ['token.text', 'token.pos', 'token.dep', 'token.head.text', 'token.head.pos', 'token.ent_type']) 
    print(text)
    for token in doc:
      a = token.text, token.pos_, token.dep_, token.head.text, token.head.pos_, token.ent_type_
      a_r += a
    return a_r

###
spacy_string = print_tokens(string)

###
print(spacy_string[0:6]) #teste
