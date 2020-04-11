from flask import Flask, render_template, request
from wtforms import Form, TextAreaField, validators

#Usando wtforms nós extendemos a função index, criando um campo de texto que será incluido na pagina através da classe TextAreaField
#que automaticamente ja checa quando o usuario insere um input valido ou não.

app = Flask(__name__)

class HelloForm(Form):
    sayhello = TextAreaField('', [validators.DataRequired()])

@app.route('/')
def index():
    form = HelloForm(request.form)
    return render_template('first_app.html', form=form)

#O metodo 'POST' é usado para transportar os dados do formulario para o servidor
#Definindo uma nova função (hello) que será responsável por renderizar a  pagina HTML hello.html após a validação do formulario
@app.route('/hello', methods=['POST'])
def hello():
    form = HelloForm(request.form)
    if request.method == 'POST' and form.validate():
        name = request.form['sayhello']
        return render_template('hello.html', name=name)
    return render_template('first_app.html', form=form)


#O argumento debug=True ativa o depurador do FLASK, o que será útil futuramente.
if __name__ == '__main__':
    app.run(debug=True)
