from hazm import *
import re


def load_stopwords():

    f = open("stopwords-fa.txt", "r",encoding='utf8')
    stopwords = f.read()
    stopwords = stopwords.split('\n')
    stopwords = set(stopwords)
    stopwords = list(stopwords)
    return stopwords


def clean_doc(doc):
    puncs = ['،', '.', ',', ':', ';', '"', "'", '/', '\\', '_','-']
    unwanted = load_stopwords()
    tokenized_pro_one = []
    tokenized_pro_two = []
    tokens =[]
    normalizer = Normalizer()
    normalized = normalizer.normalize(text)
    rawtokenized =word_tokenize(normalized)
    for t in rawtokenized:
        temp = t
        for p in puncs:
            temp = temp.replace(p,'')
        tokenized_pro_one.append(temp)

    for t2 in tokenized_pro_one:
        temp = t2
        for u in unwanted:
            if(temp == u):
                temp = temp.replace(u,'')
        tokenized_pro_two.append(temp)
    tokens = tokenized_pro_two
    tokens = [w for w in tokens if not len(w) <= 1]
    tokens = [w for w in tokens if not w.isdigit()]
    return tokens