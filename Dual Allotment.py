#!/usr/bin/env python
# coding: utf-8

# In[391]:


import pandas as pd
import numpy as np


# In[392]:


df=pd.read_csv('./data.csv')


# In[393]:


df.head()


# In[394]:


df.sort_values(by=['N. CGPA'], ascending=False)


# In[395]:


branch = {} 
details = {}


# In[396]:


for i in range(8):
    if(int(df.iat[4+i,13]) != 0):
        branch[df.iat[4+i,12]] = int(df.iat[4+i,13])
        if(df.iat[4+i,12] != "Total"):
            details[df.iat[4+i,12]] = [0]*7
            details[df.iat[4+i,12]][6] = int(df.iat[4+i,13])


# In[397]:


branch
df.rename(columns = {'Unnamed: 10':'allotment'}, inplace = True)


# In[398]:


branch


# In[399]:


details


# In[400]:


df


# In[401]:


# filled || start cgpa || end cgpa || start pbi || end pbi || end id || seats


# In[402]:


for ind in df.index:
    for i in range(6):
        br = df['PR' + str(i+1)][ind]
        if(branch[str(br)]>0):
            df['allotment'][ind] = br
            branch[br] = branch[br] - 1
            details[br][2] = df['N. CGPA'][ind] # end CGPA
            details[br][5] = df['id No'][ind]   # end ID
            details[br][0] = details[br][0]+1   # Seats filled
            details[br][4] = df['PBI'][ind]     # end PBI            
            if(details[br][6] == branch[br]+1):
                details[br][1] = df['N. CGPA'][ind] # start CGPA
                details[br][3] = df['PBI'][ind]     # start PBI
            print('Seats of ' + str(br) + ' are remained only ' + str(branch[str(br)]))
            break
            
            


# In[403]:


# Schema
# filled || start cgpa || end cgpa || start pbi || end pbi || end id || seatsdf
details


# In[404]:


# put it into loop if schema is finalized
for i in range(7):
    for j in range(5):
        if(df.iat[4+i,12] ==df.iat[4+i,12]):
            df['Unnamed: '+ str(14+j)][4+i] = details[df.iat[4+i,12]][j]
    


# In[405]:


df


# In[406]:


df.to_csv('allotment_final.csv', encoding='utf-8', index=False)

