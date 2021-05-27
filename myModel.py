import pandas as pd
import numpy as np

from sklearn.svm import SVC
from sklearn.linear_model import LogisticRegression
from sklearn import svm

from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

# import data
df = pd.read_csv('abusive_language_data.csv')

df = df.dropna()

# drop the rows where the model and human annotator disagree

df = df[df['model_wrong'] == False]

cond = df['label'] == 'hate'

# function to lowercase all words:

def make_lower(a_string):
    return a_string.lower()

# add a new column that renames 'hate' as 'abusive', 'nothate' as 'not abusive'

df['new_label'] = np.where(cond, 'abusive', 'not abusive')

# lower case text column only, leave punc in, don't stem words

df['text_clean'] = df['text'].apply(make_lower)

# define variables:

X = df['text_clean'].values

y = df['new_label'].values

# vectorize 

vectorizer = TfidfVectorizer(ngram_range=(1, 2))
X = vectorizer.fit_transform(X)

model = svm.SVC(probability=True)

model.fit(X, y)

# NAME YOUR MODELS 
tc = 'text-classifer_me.pkl'
vect = 'vectorizer_me.pkl'

# EXPORT AND SAVE YOUR MODELS USING YOUR FILENAME
pickle.dump(model, open(tc, 'wb'))
pickle.dump(vectorizer, open(vect, 'wb'))