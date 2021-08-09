from src.pyate import combo_basic
from src.pyate.term_extraction_pipeline import TermExtractionPipeline
nlp.add_pipe(TermExtractionPipeline())

def combobasic_com_sw(document): 
    cb_index = []
    cb_value = [] 
    doc = nlp(document)
    cb_dataframe = pd.DataFrame(columns = ['string', 'value']) 
    cb_original = doc._.combo_basic.sort_values(ascending=False)
    
    for i in cb_original.index: 
      cb_index.append(i)
    
    for j in cb_original: 
      cb_value.append(j)
    
    cb_resultado = {cb_index[k]: cb_value[k] for k in range(len(cb_index))} 
    
    return cb_resultado, cb_index, cb_value

###
[combo_basic_com_stop_words,cb_indice, cb_valores] = combobasic_com_sw(string) 

###
#sem stop words
k = []
for x in combo_basic_com_stop_words:
  if x not in stopwords:
    k.append(x)
    print("'" + str(x)+"'"+ ': '+ str(combo_basic_com_stop_words[x])) 
