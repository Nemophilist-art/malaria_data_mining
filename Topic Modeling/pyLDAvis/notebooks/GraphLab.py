#!/usr/bin/env python
# coding: utf-8

# # Visualizing GraphLab's LDA TopicModel with pyLDAvis
# 
# This is an example of how to use [`pyLDAvis`](https://github.com/bmabey/pyLDAvis) [helper functions](https://pyldavis.readthedocs.org/en/latest/modules/API.html#module-pyLDAvis.graphlab) to visualize a GraphLab Create Topic Model model. For our example model we will be extending the example provided by [GraphLab's own documenation](https://dato.com/products/create/docs/generated/graphlab.topic_model.create.html).

# In[2]:


import graphlab as gl
import pyLDAvis
import pyLDAvis.graphlab


# In[3]:


# turn on automatic rendering of visualizations
pyLDAvis.enable_notebook()


# In[4]:


docs = gl.SArray('http://s3.amazonaws.com/GraphLab-Datasets/nytimes')


# In[7]:


get_ipython().run_line_magic('pinfo', 'gl.topic_model.create')


# In[8]:


get_ipython().run_cell_magic('time', '', 'topic_model = gl.topic_model.create(docs, num_topics=15, num_iterations=3000)\n')


# In[58]:


pyLDAvis.graphlab.prepare(topic_model, docs)

