from GestaoGUI.persistencia.dal import configuracao_inicial
from GestaoGUI.visao.Login import Login

if __name__ == "__main__":
    configuracao_inicial()
    login = Login()
    login.mainloop()
