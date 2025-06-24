#!/usr/bin/env python
# coding: utf-8

# # `pyLDAvis.lda_model`
# 
# pyLDAvis now also supports LDA application from scikit-learn. Let's take a look into this in more detail. We will be using the 20 newsgroups dataset as provided by scikit-learn.

# In[1]:


import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning) 
warnings.filterwarnings('ignore', category=FutureWarning) 
warnings.filterwarnings('ignore', category=UserWarning)


# In[2]:


import pyLDAvis
import pyLDAvis.lda_model
pyLDAvis.enable_notebook()


# In[3]:


from sklearn.datasets import fetch_20newsgroups
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
from sklearn.decomposition import LatentDirichletAllocation


# ## Load 20 newsgroups dataset
# 
# First, the 20 newsgroups dataset available in sklearn is loaded. As always, the headers, footers and quotes are removed.

# In[4]:


newsgroups = fetch_20newsgroups(remove=('headers', 'footers', 'quotes'))
docs_raw = newsgroups.data
print(len(docs_raw))


# ## Convert to document-term matrix
# 
# Next, the raw documents are converted into document-term matrix, possibly as raw counts or in TF-IDF form.

# In[5]:


tf_vectorizer = CountVectorizer(strip_accents = 'unicode',
                                stop_words = 'english',
                                lowercase = True,
                                token_pattern = r'\b[a-zA-Z]{3,}\b',
                                max_df = 0.5, 
                                min_df = 10)
dtm_tf = tf_vectorizer.fit_transform(docs_raw)
print(dtm_tf.shape)


# In[6]:


tfidf_vectorizer = TfidfVectorizer(**tf_vectorizer.get_params())
dtm_tfidf = tfidf_vectorizer.fit_transform(docs_raw)
print(dtm_tfidf.shape)


# ## Fit Latent Dirichlet Allocation models
# 
# Finally, the LDA models are fitted.

# In[7]:


# for TF DTM
lda_tf = LatentDirichletAllocation(n_components=20, random_state=0)
lda_tf.fit(dtm_tf)
# for TFIDF DTM
lda_tfidf = LatentDirichletAllocation(n_components=20, random_state=0)
lda_tfidf.fit(dtm_tfidf)


# ## Visualizing the models with pyLDAvis

# In[8]:


pyLDAvis.lda_model.prepare(lda_tf, dtm_tf, tf_vectorizer)


# In[9]:


pyLDAvis.lda_model.prepare(lda_tfidf, dtm_tfidf, tfidf_vectorizer)


# ### Using different MDS functions
# 
# With `sklearn` installed, other MDS functions, such as MMDS and TSNE can be used for plotting if the default PCoA is not satisfactory.

# In[10]:


pyLDAvis.lda_model.prepare(lda_tf, dtm_tf, tf_vectorizer, mds='mmds')


# In[11]:


pyLDAvis.lda_model.prepare(lda_tf, dtm_tf, tf_vectorizer, mds='tsne')

