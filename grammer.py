import re
import string
import numpy as np
from gingerit.gingerit import GingerIt
import nltk
from nltk.corpus import stopwords
stop_words = stopwords.words("english")


# check for grammer and spelling errors and return the number of corrections
def check(filename):
    f = word(filename, 'sentence')
    corrections = 0
    for s in f:
        g = GingerIt()
        h = g.parse(s)
        corrections += len(h['corrections'])
    return [corrections]

def word(filename, final_type): # function to tokenize text 
        tok_sent = nltk.sent_tokenize(filename)
        tok_word = []
        clean = []
        reclean = []
        for s in tok_sent:
            tok_word.append(nltk.word_tokenize(s))
        final_text = []
        for i in tok_sent:
            i = i.replace("\n", " ")
            clean.append(i)
        clean = np.vectorize(remove_pattern)(clean, "http[s]?://\S+")

        for i in clean:
            i = str(i)
            reclean.append(i)

        for w in tok_word:
            if w not in stop_words:
                final_text.append(w)
        if final_type == 'sentence':
            return reclean
        elif final_type == 'word':
            return final_text

def remove_pattern(input_txt, pattern):
    r = re.findall(pattern, input_txt)
    for i in r:
        input_txt = re.sub(i, '', input_txt)

    return input_txt
