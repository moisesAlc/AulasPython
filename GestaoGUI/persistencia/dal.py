from GestaoGUI.persistencia.automoveis_db import existem_dados_sqlite3
from GestaoGUI.persistencia.mongo.connect import make_connection


def config_bd():
    if existem_dados_sqlite3():
        print("Conectado ao banco local com sucesso.")
    else:
        print("Não foi possível conectar ao banco local.")
    if make_connection():
        print("Conectado ao banco remoto com sucesso.")
    else:
        print("Não foi possível conectar ao banco remoto.")
