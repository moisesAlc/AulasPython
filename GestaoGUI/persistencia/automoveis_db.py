from GestaoGUI.modelos.Automovel import Automovel
import sqlite3

con = sqlite3.connect("persistencia/dados.db")
cursor = con.cursor()


def existem_dados():
    result = cursor.execute("SELECT * FROM automoveis")
    if result.fetchone():
        print(result.fetchone())
        return True
    else:
        return False


def retorna_automoveis():
    result = cursor.execute("SELECT * FROM automoveis").fetchall()
    automoveis = []
    for automovel in result:
        '''print(automovel)
        novo_automovel = Automovel()
        novo_automovel.nome = automovel'''

        automoveis.append(Automovel(automovel))
    return automoveis
