#!/usr/bin/env python
# coding: utf-8

# In[174]:


import os
import subprocess
#from IPython.core.interactiveshell import InteractiveShell
#InteractiveShell.ast_node_interactivity = "all"
import numpy as np


# In[175]:


my_dict = {}

names = ['files','readlinks']

for name in names:

    my_dict[name] = []

    with open(os.path.expanduser('~/scripts/'+name)) as file:
        for item in file:
            my_dict[name].append(item.splitlines()[0])
        


# In[176]:


my_dict['projects_files'] = []
my_dict['projects_readlinks'] = []


for i in range(len(my_dict['readlinks'])):
    if '/projects' in my_dict['readlinks'][i]:
        my_dict['projects_readlinks'].append(my_dict['readlinks'][i])
        my_dict['projects_files'].append(my_dict['files'][i])
        


# In[177]:


for i in range(len(my_dict['projects_readlinks'])):
    my_dict['projects_readlinks'][i] = \
    my_dict['projects_readlinks'][i].replace('/projects/ocean','/gws/nopw/j04/tids/OCEAN')


# In[178]:


names = ['files','readlinks']

for name in names:
    
    with open(os.path.expanduser('~/scripts/projects_'+name), 'w') as fp:
        for item in my_dict['projects_'+name]:
            fp.write("%s\n" % item)


# In[ ]:





# In[ ]:





# In[ ]:




