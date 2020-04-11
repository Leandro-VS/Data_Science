
# coding: utf-8

# In[1]:


def menor_nome(lista_nomes):
    x = []
    d = []
    for i in range(len(lista_nomes)):
        x.append(len(lista_nomes[i].strip()))
    
    aux = min(x)
    for i in range(len(lista_nomes)):
        if aux == len(lista_nomes[i].strip()):
            d.append(lista_nomes[i].strip().capitalize())
    y = d[0]
    return y

