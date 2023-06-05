from GestaoGUI.visao.Login import Login
from GestaoGUI.visao.MainWindow import MainWindow
from GestaoGUI.persistencia.banco import configuracao_inicial

if __name__ == "__main__":
    configuracao_inicial()
    MainWindow().mainloop()
