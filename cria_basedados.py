import sqlite3


conn = sqlite3.connect('basedados.db')

cursor = conn.cursor()

cursor.execute('''
create table cadastro_clientes(
    id integer primary key autoincrement,
    nome text not null,
    sobrenome text not null,
    cpf text not null
)''')

cursor.execute('insert into cadastro_clientes(Nome,sobrenome,cpf) values ("João","Cavichiolli","1222")')


cursor.execute('insert into cadastro_clientes(Nome,sobrenome,cpf) values ("Pedro","Silva","1333")')

conn.commit()
conn.close()