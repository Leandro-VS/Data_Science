
# coding: utf-8

# In[3]:


def maiusculas(frase):
    x = []
    d = ""
    frase.split()
    for i in range(len(frase)):
        if ord(frase[i]) == ord(frase[i].upper()) and ord(frase[i]) > 65:
            x.append(frase[i])
    
    for i in range(len(x)):
        d += x[i]
    return d

