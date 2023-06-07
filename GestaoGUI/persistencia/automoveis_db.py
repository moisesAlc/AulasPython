import sqlite3

con = sqlite3.connect("persistencia/dados.db")
cursor = con.cursor()


def existem_dados():
    result = cursor.execute("SELECT * FROM automoveis")
    print(result.fetchone())

