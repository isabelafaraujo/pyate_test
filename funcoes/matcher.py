import spacy
from spacy.tokenizer import Tokenizer
from spacy.matcher import Matcher

matcher = Matcher(nlp.vocab)
matches = matcher(doc)

dataframe = pd.read_csv('/content/drive/My Drive/ColabNotebooks/txt.txt',sep='delimiter' , header = None) #todos textos sobre diabetes

###
def get_noun_patterns():
    
    return [[
                {'POS': {'IN': ['NOUN', 'PROPN']}},
                {'POS': {'IN': ['ADP', 'ADJ']},'OP':'?'},
                {'POS': {'IN': ['DET', 'PRON']},'OP':'?'},
                {'POS': {'IN': ['NOUN', 'PROPN']},'OP':'?'},
                {'POS': {'IN': ['ADP', 'ADJ']},'OP':'?'}
            ]]

def get_complements_patterns():
    
    return [[
                {'POS': 'ADP','OP':'?'},
                {'POS': {'IN': ['DET', 'PRON']},'OP':'?'},
                {'POS': 'PUNCT','OP':'?'},
                {'POS': {'IN': ['DET', 'PRON']},'OP':'?'},
                {'POS': 'PUNCT','OP':'?'},
                {'POS': {'IN': ['NOUN', 'PROPN', 'ADV']}}
            ]]

def get_pleads_patterns():
    
    return [[
                {'POS': 'ADP','OP':'?'},
                {'POS': {'IN': ['DET', 'PRON']}},
                {'POS': 'PUNCT','OP':'?'},
                {'POS': {'IN': ['DET', 'PRON']},'OP':'?'},
                {'POS': 'PUNCT','OP':'?'},
                {'POS': {'IN': ['NOUN', 'PROPN']}}
            ]]


def print_candidates(path, pattern):
    m_r = []     
    doc1 = nlp(path)
    matcher = Matcher(vocab) 
    matcher.add("complements", pattern) 
    matches = matcher(doc1)
    #print(doc1)
    m_r = []
    for i in range(0,len(matches)):
      start = matches[i][1]
      end = matches[i][2]
      span = doc1[start:end]
      text = ['{} ({})'.format(token.text, token.pos_) for token in span]
      r = (start, end, text)
      m_r.append(r)
      #print('Match from %s to %s: %s' % (start, end, text))

    return m_r

###
noun_patterns_df = pd.DataFrame(print_candidates(str(dataframe),get_noun_patterns()),columns=['start','end','text'])
noun_patterns_string = pd.DataFrame(print_candidates(string,get_noun_patterns()),columns=['start','end','text'])
complements_patterns_string = pd.DataFrame(print_candidates(string,get_complements_patterns()),columns=['start','end','text'])
complements_patterns_df = pd.DataFrame(print_candidates(str(dataframe),get_complements_patterns()),columns=['start','end','text'])
pleads_patterns_string = pd.DataFrame(print_candidates(str(string),get_pleads_patterns()),columns=['start','end','text'])
pleads_patterns_df = pd.DataFrame(print_candidates(str(dataframe),get_pleads_patterns()),columns=['start','end','text'])


