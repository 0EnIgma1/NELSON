import pickle
import sklearn
from sklearn.feature_extraction.text import CountVectorizer
from  sklearn.feature_extraction.text import TfidfVectorizer
from sklearn import *
import joblib

cv=CountVectorizer(min_df=0,max_df=1,binary=False,ngram_range=(1,3))
tv=TfidfVectorizer(min_df=0,max_df=1,use_idf=True,ngram_range=(1,3))

model = joblib.load('senti')

#self._vectorizer = vectorizer

a = []

for i in range(6209090):
    a = a + ['a']

s1 = ["a b good"]
tv.fit(a)
x = tv.transform(a)

model.predict(x)