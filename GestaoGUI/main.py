from GestaoGUI.persistencia.dal import config_bd
from GestaoGUI.visao.Login import Login


if __name__ == "__main__":
    config_bd()
    login = Login()
    login.mainloop()
