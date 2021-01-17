#!/usr/bin/env python
# coding: utf-8

# In[2]:


import copy


# In[3]:


my_dict = {'a': [1, 2, 3], 'b': [4, 5, 6]}


# In[4]:


my_copy = my_dict.copy()


# In[5]:


id(my_dict)


# In[6]:


id(my_copy)


# In[7]:


id(my_copy['a'])


# In[8]:


id(my_dict['a'])


# In[9]:


my_copy = {key: value[:] for key, value in my_dict.items()}


# In[10]:


id(my_copy['a'])


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




