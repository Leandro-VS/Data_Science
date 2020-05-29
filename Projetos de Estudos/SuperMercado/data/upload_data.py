import os
import pandas as pd

#Endereços da base .csv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

df = pd.read_csv("Compras_Mercado.csv")
print(df.head())