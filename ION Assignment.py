
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


import seaborn as sns


# In[28]:


myfile='D:\Mufaddal\Data Science\Assignment file for Data Analyst - assignment file.csv'
pt=pd.read_csv(myfile,sep=",")


# In[29]:


pt


# In[30]:


sns.heatmap(pt.corr())


# In[31]:


pt.corr()

