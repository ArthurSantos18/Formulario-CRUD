import sqlite3 as sql

# Conectando ou criando um banco de dados
con = sql.connect('database.db')

# Create
def create_data(data):
    with con:
        cursor = con.cursor()
        query = "INSERT INTO pessoas(nome, email, dia, sexo) VALUES (?, ?, ?, ?)"
        cursor.execute(query, data)

# Read
def read_data():
    lista = []
    with con:
        cursor = con.cursor()
        query = "SELECT * FROM pessoas"
        cursor.execute(query)
        datas = cursor.fetchall()
        
        for data in datas:
            lista.append(data)
    return lista

# Update
def update_data(data):
    with con:
        cursor = con.cursor()
        query = "UPDATE pessoas SET nome=?, email=?, dia=?, sexo=? WHERE id=?"
        cursor.execute(query, data)

# Delete
def delete_data(data):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM pessoas WHERE id=?"
        cursor.execute(query, data)
