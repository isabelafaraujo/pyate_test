!pip install nltk

import nltk
from nltk.corpus import floresta
from nltk.corpus import mac_morpho
from nltk.corpus import machado
from nltk.corpus import machado
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk.corpus import words
from nltk.tokenize import WordPunctTokenizer
from string import punctuation
import pandas as pd
from nltk.tokenize import sent_tokenize

import nltk
nltk.download()

#!pip install -U nltk 

'''
- averaged_perceptron_tagger
- floresta
- mac_morpho
- machado
- punkt
- stopwords
- wordnet
- words
'''

###
stopwords = set(nltk.corpus.stopwords.words('portuguese') + list(punctuation))
