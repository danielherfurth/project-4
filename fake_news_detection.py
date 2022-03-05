from sklearn.feature_extraction.text import CountVectorizer
import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split as tts
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import TfidfVectorizer
import pickle
from sklearn.decomposition import LatentDirichletAllocation

news = pd.read_csv('data/train_processed.csv')
x = news['author_text_clean']
y = news['label']

vect = CountVectorizer(max_df=0.8, min_df=2, stop_words='english')
lda_topics = vect.fit_transform(df['author_text_clean'].values.astype('U'))

x_train, x_test, y_train, y_test = tts(x, y, test_size=0.2)

pipeline = Pipeline([('tfidf', TfidfVectorizer(stop_words='english')),
                     ('nbmodel', MultinomialNB())])

pipeline.fit()
