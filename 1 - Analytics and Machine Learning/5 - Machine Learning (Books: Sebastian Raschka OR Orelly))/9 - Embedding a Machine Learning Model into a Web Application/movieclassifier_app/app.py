from flask import Flask, render_template, request, url_for
from wtforms import Form, TextAreaField, validators
import pickle
import sqlite3
import os
import numpy as np
# import HashingVectorizer from local dir
from vectorizer import vect

#Importando a lib que fará o update do modelo a cada(lote) feedback
from update import update_model


app = Flask(__name__)

#Preparando o classificador
cur_dir = os.path.dirname(__file__) #diretório atual
#Carregando o modelo(LogisticRegression)
clf = pickle.load(open(os.path.join(cur_dir, 'pkl_objects', 'classifier.pkl'), 'rb'))
#Carregando o Database
db = os.path.join(cur_dir, 'reviews.sqlite')

#Função que retorna a label prevista pelo modelo assim como a probabilidade da mesma
def classify(document):
    label = {0: 'negativo', 1: 'positivo'}
    X = vect.transform([document])
    y = clf.predict(X)[0]
    proba = np.max(clf.predict_proba(X))
    return label[y], proba

#Atualiza o modelo treinando-o com um review e uma label dada
def train(document, y):
    X = vect.transform([document])
    clf.partial_fit(X, [y])
    
#Armazena o submit review no nosso database junto com a label e o timestamp
def sqlite_entry(path, document, y):
    conn = sqlite3.connect(path)
    c = conn.cursor()
    #Criando uma tabela com 3 colunas
    #c.execute('CREATE TABLE review_db'\
     #                        '(review TEXT, sentiment INTEGER, date TEXT)')
    #Inserindo dados na tabela
    c.execute("INSERT INTO review_db (review, sentiment, date)"\
             "VALUES (?, ?, DATETIME('now'))", (document, y))
    conn.commit()
    conn.close()

#Flask

"""
Classe que instancia o TextAreaField, que será renderizado no reviewform.html, e esta classe é renderizada pela
função index
"""
class ReviewForm(Form):
    #Reviews validos com pelo menos 15 caracteres
    moviereview = TextAreaField('', [validators.DataRequired(), validators.length(min=15)])
    
@app.route('/')
def index():
    form = ReviewForm(request.form)
    return render_template('reviewform.html', form=form)

"""
A função results busca o review passado pelo usuário e passa para o classificador fazer a previsão do sentimento
Tal previsão será renderizada no results.html(template)
"""
@app.route('/results', methods=['POST'])
def results():
    form = ReviewForm(request.form)
    if request.method == 'POST' and form.validate():
        review = request.form['moviereview']
        y, proba = classify(review)
        return render_template('results.html', 
                               content=review,
                               prediction=y, 
                               probability=round(proba*100, 2))
    return render_template('reviewform.html', form=form)

"""
Busca a previsão feita pelo modelo do arquivo results.html, se o usuário clica no botão de Correto ou Incorreto, 
e transforma a previsão de sentimento devolta para um inteiro que será usado para atualizar o classificador
através da função train().
Há também uma nova entrada para o banco de dados através da sqlite_entry que recebe o feedback do usuario, e por
último um agradecimento é feito ao usuário caso ele use o feedback.
"""
@app.route('/thanks', methods=['POST'])
def feedback():
    feedback = request.form['feedback_button']
    review = request.form['review']
    prediction = request.form['prediction']
    
    inv_label = {'negativo': 0, 'positivo': 1}
    y = inv_label[prediction]
    
    if feedback == 'Incorreto':
        y = int(not(y))
    
    train(review, y)
    sqlite_entry(db, review, y)
    return render_template('thanks.html')

if __name__ == '__main__':
	clf = update_model(db_path=db, model=clf, batch_size=10000)

if __name__ == '__main__':
    app.run()
