
# coding: utf-8

# In[1]:


def conta_letras(frase, contar= "vogais"):
    count = 0
    if contar == "vogais":
        for i in range(len(frase)):
            if frase[i] == 'a' or frase[i] == 'A' or frase[i] == 'e' or frase[i] == 'E' or frase[i] == 'i' or frase[i] == 'I' or frase[i] == 'o' or frase[i] == 'O' or frase[i] == 'u' or frase[i] == 'U':
                 count += 1
        return count
    elif contar == "consoantes":
        x = frase.split()
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j] != 'a' and x[i][j] != 'A' and x[i][j] != 'e' and x[i][j] != 'E' and x[i][j] != 'i' and x[i][j] != 'I' and x[i][j] != 'o' and x[i][j] != 'O' and x[i][j] != 'u' and x[i][j] != 'U':
                    count += 1
        return count

