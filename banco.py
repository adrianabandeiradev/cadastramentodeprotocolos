# importanto SQLITE
import sqlite3 as lite


# Criando conexão
con = lite.connect('dados.db')

# criando tabela
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE formulario(id INTEGER PRIMARY KEY AUTOINCREMENT, cliente TEXT, protocolo TEXT, tipo_protocolo TEXT, dia_en DATE, status TEXT, observacao TEXT)")