### O APP.PY e o arquivo de configuração principal do projeto do Flask ##

from flask import Flask,render_template,request,url_for,redirect
import sqlite3 
from flask_mysqldb import MySQL

app = Flask(__nam

## Criar a string do conexão do MYSQL

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'python'
app.config['MYSQL_PASSWORD'] = 'python123'
app.config["MYSQL_DB"] = 'banco01'

mysql = MySQL(app)




## Routes ou rotas que são caminhos da aplicação web

# A pagina principal de uma aplicacao web  e tambem conhecido como /
# ou raiz 

#@app.route('/')
#def hello():
#    return "Olá Estou Executando a Pagina Inicial com FLASK"

## Renderizando a Pagina Inicial com 1 template HTML

## Vamos criar a função de conexão com banco de dados

def get_db_connection():
    conn = sqlite3.connect('basedados.db')
    conn.row_factory = sqlite3.Row
    return conn





@app.route('/')
def index():
    return render_template('index.html')


@app.route('/clientes')
def clientes():
    return "Olá Pagina de Clientes"

## Para o front se comunicar e interagir com o Backend
# Ele usa os metodos get e post
# GET ele busca informação do backend e tras para o frontend ou para a telas

# POST ele leva a informaçaõ inserida no front pelo usuario e leva para o 
# Backend


## Rotas para as outras urls do FrontEnd


@app.route('/listaclientes',methods=('GET',"POST"))
def listaclientes():
    cursor = mysql.connection.cursor()
    cursor.execute('select * from clientes')
    clientesback = cursor.fetchone()
    cursor.close()
    return render_template('listaclientes.html',clientes=clientesback) # interliga o front com o back


@app.route('/addclientes',methods=("GET","POST"))
def addclientes():
    if request.method == "POST":
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        cursor = mysql.connection.cursor()
        cursor.execute('insert into clientes (nome,sobrenome,cpf) values (?,?,?)',(nome,sobrenome,cpf))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    return render_template('addclientes.html')

