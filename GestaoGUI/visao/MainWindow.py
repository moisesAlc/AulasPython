import tkinter as tk
import tkinter.ttk as ttk
from GestaoGUI.visao.Detail import Detail


def darkstyle(root):
    """ Return a dark style to the window"""
    style = ttk.Style(root)
    root.tk.call('source', r'.\\temas\\tkBreeze\\breeze-dark\\breeze-dark.tcl')
    style.theme_use('breeze-dark')
    return style


class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Gestão de Automóveis')

        """ Constantes """
        self.pady = 15
        self.font = 'Helvetica'
        self.font_size = 14

        style = darkstyle(self)
        style.configure('my.TButton', font=(self.font, self.font_size))

        # configure the details frame
        self.detail_frame = Detail(self).pack(ipadx=20, ipady=20)
