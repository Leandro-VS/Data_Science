
# coding: utf-8

# In[1]:


#retorna o nome passado em maiusculo
def Mod1(nome):
    return nome.upper()


# In[19]:


#retorna a força aplicada, dada a massa do corpo, se for na Terra acc = g
def Mod2(mass, acceleration = 9.8):
    f = mass * acceleration
    print("F =", f)

