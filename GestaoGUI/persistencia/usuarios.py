import sqlite3

con = sqlite3.connect("persistencia/dados.db")
cursor = con.cursor()


def verifica_login(login: str, senha: str):
    select_query = """SELECT * FROM usuarios WHERE login = ? AND password = ?"""
    cursor.execute(select_query, (login, senha))
    result = cursor.fetchone()
    if result:
        return True
    else:
        return False
