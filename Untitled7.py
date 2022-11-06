#!/usr/bin/env python
# coding: utf-8

# In[3]:


from pyopenms import*


# In[5]:


s=AASequence.fromString("VAKA")
mono_W_s=s.getMonoWeight()
print(mono_W_s)


# In[8]:


mono_W_aa=0
for aa in s:
    mono_W_aa=mono_W_aa+aa.getMonoWeight()
    
print(g)    


# In[10]:


if mono_W_s>mono_W_aa:
    print("The full weight of sequence is greater than summation of monoweight for each amino acid ")
else:
    print("The summation of monoweight foreach amino acid is greater than Full weight of sequence ")


# In[ ]:




