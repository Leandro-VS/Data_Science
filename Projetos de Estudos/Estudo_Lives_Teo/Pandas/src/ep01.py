import pandas as pd

# Importando um csv
pathfile_csv = "/home/leandro/Documents/Data_Science/Projetos de Estudos/Estudo_Lives_Teo/Pandas/data/tb_candidatura_2018.csv"
df_candidatura = pd.read_csv(pathfile_csv, sep=";")
df_candidatura.head()

# Importando um xlsx
pathfile_xlsx = "/home/leandro/Documents/Data_Science/Projetos de Estudos/Estudo_Lives_Teo/Pandas/data/tb_declaracao_2018.xlsx"
df_declaracao = pd.read_excel(pathfile_xlsx)
df_declaracao.head()

# Observações
# loc e iloc
df_candidatura.loc[29140:29145] # gets rows (or columns) at particular positions in the index (so it only takes integers)

df_candidatura.loc[1]# gets rows (or columns) with particular labels from the index (takes intergers and labels)
