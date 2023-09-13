import sqlite3 as sql

def create_database():
    # Conectando ou criando um banco de dados
    con = sql.connect('formulario.db')

    # Criando a tabela
    with con:
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS pessoas(
                    id INTEGER PRIMARY KEY AUTOINCREMENT, 
                    nome TEXT, 
                    email TEXT, 
                    dia DATE, 
                    sexo TEXT)''')
