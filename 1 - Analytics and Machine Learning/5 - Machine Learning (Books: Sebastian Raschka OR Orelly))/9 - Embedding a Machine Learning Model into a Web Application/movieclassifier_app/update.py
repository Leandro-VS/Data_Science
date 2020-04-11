#Libs
import pickle
import sqlite3
import numpy as np
import os

#Carregando a lib HashingVectorizer localizada no mesmo diretório
from vectorizer import vect

#Função update
#A query sql retorna resultados do banco em lotes de 10.000 por vez
def update_model(db_path, model, batch_size=10000):
    #Criando a conexão com o db e fazendo a query dos valores da tabela
    conn = sqlite3.connect(db_path)
    c = conn.cursor()
    c.execute('SELECT * from review_db')
    results = c.fetchmany(batch_size)
    
    #Treinando o modelo(parcialmente) com os dados novos vindos do banco de dados
    while results:
        data = np.array(results)
        X = data[:, 0]
        y = data[:, 1].astype(int)
        
        classes = np.array([0,1])
        X_train = vect.transform(X)
        model.partial_fit(X_train, y, classes=classes)
        results = c.fetchmany(batch_size)
        
    conn.close()
    return model

#diretório atual
cur_dir = os.path.dirname(__file__)

#Unpickle do modelo
clf = pickle.load(open(os.path.join(cur_dir, 
                                   'pkl_objects', 
                                   'classifier.pkl'), 'rb'))

#Diretório do banco de dados
db = os.path.join(cur_dir, 'reviews.sqlite')

#Atualizando o modelo
clf = update_model(db_path=db, model=clf, batch_size=10000)
