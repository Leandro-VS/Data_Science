
# coding: utf-8

# In[1]:


def primeiro_lex(vet_string):
    aux = vet_string[0] 
    for i in range(len(vet_string)):
        if aux > vet_string[i].strip():
            aux = vet_string[i].strip() 
    return aux

