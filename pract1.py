
# coding: utf-8

# In[4]:

import json
import gzip

def parse(path):
  g = gzip.open(path, 'r')
  for l in g:
    yield eval(l)
paragraph = []
for l in parse("E:/Academics/kaggle/intern/reviews_Beauty.json.gz"):
  paragraph.append(l['reviewText'] + '\n')
  


# In[29]:

from sklearn.cross_validation import train_test_split


# In[30]:

train, test = train_test_split(paragraph, train_size = 0.8)


# In[31]:

from sklearn.feature_extraction.text import CountVectorizer


# In[59]:

count_vect = CountVectorizer()
train_vect = count_vect.fit(train)
train_vect = count_vect.transform(train)


# In[33]:

train_vect.shape


# In[34]:

count_vect.vocabulary_.get(u'happy')


# In[35]:

from sklearn.feature_extraction.text import TfidfTransformer


# In[37]:

train_tfidf.shape


# In[38]:

from sklearn.datasets import load_files


# In[39]:

movie_data = r'E:\Academics\kaggle\intern\movie_reviews\movie_reviews'


# In[42]:

movie_data


# In[43]:

movie_train = load_files(movie_data, shuffle=True)


# In[44]:

import nltk
movie_vec = CountVectorizer(min_df=2, tokenizer=nltk.word_tokenize)         
movie_counts = movie_vec.fit_transform(movie_train.data)

tfidf_transformer = TfidfTransformer()
movie_tfidf = tfidf_transformer.fit_transform(movie_counts)

movie_tfidf.shape


# In[45]:

movie_vec.vocabulary_.get('love')


# In[46]:

from sklearn.naive_bayes import MultinomialNB


# In[60]:

clf = MultinomialNB().fit(movie_tfidf, movie_train.target)


# In[70]:


vectorizer_test = CountVectorizer(vocabulary=movie_vec.vocabulary_)
X_test = vectorizer_test.transform(train)


# In[71]:

y_pred = clf.predict(X_test)


# In[ ]:

f = open("E:/Academics/kaggle/intern/output/result.txt", 'w')
for review, category in zip(train, y_pred):
    f.write('%r, %s' % (review, movie_train.target_names[category]))
    print('%r, %s' % (review, movie_train.target_names[category]))






