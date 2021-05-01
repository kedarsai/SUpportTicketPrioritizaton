import nltk

nltk.download('stopwords')
stopwords=set(nltk.corpus.stopwords.words('english'))
stemmer=nltk.stem.PorterStemmer()

def tokenize(text):
    tokens=[x for x in nltk.word_tokenize(text) if len(x)>3]
    tokens=[x.lower() for x in tokens]
    stems=[stemmer.stem(item) for item in tokens if item not in stopwords]
    return stems