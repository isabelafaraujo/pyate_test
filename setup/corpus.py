import pandas as pd
import os

# Wiki em português
os.environ['KAGGLE_CONFIG_DIR'] = "/content/drive/My Drive/kaggle"
path = '/content/drive/My Drive/kaggle'
os.chdir(path)
!kaggle datasets download -d tiarles/wiki-portugues
!unzip \*.zip  && rm *.zip

#todo texto
dg = open('/content/drive/My Drive/kaggle/full.txt')
dic_geral = str(dg)


#corpus generico em portugues
d = pd.read_fwf('/content/pyate/src/pyate/txt.csv')
d.to_csv('/content/pyate/src/pyate/default_general_domain.pt.csv')
