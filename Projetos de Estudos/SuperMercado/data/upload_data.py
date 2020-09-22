import os
import pandas as pd

#Endereços da base .csv
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')

# df = pd.read_csv(DATA_DIR + '/Compras_Mercado.csv')
# df.head()

file = open('test.txt', 'w')