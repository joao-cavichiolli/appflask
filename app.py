### O APP.PY e o arquivo de configuração principal do projeto do Flask ##

from flask import Flask,render_template,request,url_for,redirect
import sqlite3 
from flask import jsonify # para retornar em formato JSON

app = Flask(__name__)

app.config['JSON_SORT_KEYS']=False
app.config['JSON_AS_ASCII'] = False

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
    conn = get_db_connection()
    clientesback = conn.execute('select * from cadastro_clientes').fetchall()
    conn.close()
    return render_template('listaclientes.html',clientes=clientesback) # interliga o front com o back


@app.route('/addclientes',methods=("GET","POST"))
def addclientes():
    if request.method == "POST":
        nome = request.form['nome']
        sobrenome = request.form['sobrenome']
        cpf = request.form['cpf']
        conn= get_db_connection()
        conn.execute('insert into cadastro_clientes (nome,sobrenome,cpf) values (?,?,?)',(nome,sobrenome,cpf))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))
    return render_template('addclientes.html')

@app.route('/enderecos/<string:nome>,<string:end>')
def hello(nome,end):
    return jsonify({'Nome':nome,"Endereco":end})