import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from GestaoGUI.persistencia.usuarios import verifica_login
from GestaoGUI.visao.MainWindow import *


def darkstyle(root):
    """ Return a dark style to the window"""
    style = ttk.Style(root)
    root.tk.call('source', r'.\\temas\\tkBreeze\\breeze-dark\\breeze-dark.tcl')
    style.theme_use('breeze-dark')
    return style


class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        """ Constantes """
        self.pady = 15
        self.font = 'Helvetica'

        """ The window with the darkstyle """
        self.title("Gestão de Automóveis - Login")
        self.resizable(True, True)
        self.geometry("600x350")
        self.iconbitmap(r'.\\img\\icone.ico')
        self.logo = tk.PhotoImage(file=r'.\\img\\logo20dpi.png')

        style = darkstyle(self)
        style.configure('my.TButton', font=(self.font, 14))

        frame_logo_welcome = ttk.Frame(self)
        logo = ttk.Label(
            frame_logo_welcome,
            anchor="w",
            image=self.logo)
        welcome = ttk.Label(
            frame_logo_welcome,
            text="Gestão de Automóveis",
            font=(self.font, 30),
            anchor="e")
        logo.pack(side="left")
        welcome.pack(side="right", padx=15)
        frame_logo_welcome.pack(pady=self.pady + 10)

        frame_authorization = ttk.Frame(self)

        login_label = ttk.Label(
            frame_authorization,
            text="Login",
            font=(self.font, 12)
        )

        login_entry = ttk.Entry(
            frame_authorization,
            foreground='#666699',
            justify="center",
        )
        login_entry.insert(0, 'E-mail/Username')

        password_label = ttk.Label(
            frame_authorization,
            text="Senha",
            font=(self.font, 12)
        )

        password_entry = ttk.Entry(
            frame_authorization,
            show="●",
            width=20,
            foreground='#666699',
            justify="center",
        )
        password_entry.insert(0, '******')

        login_label.grid(row=0, column=0, padx=10, pady=self.pady)
        login_entry.grid(row=0, column=1, padx=10, pady=self.pady)
        password_label.grid(row=1, column=0, padx=10, pady=self.pady)
        password_entry.grid(row=1, column=1, padx=10, pady=self.pady)

        frame_authorization.pack()

        button = ttk.Button(
            self,
            text="Login",
            width=20,
            command=lambda: self.btn_login_click(login_entry.get(), password_entry.get())
        )

        button.pack(pady=self.pady)

    def btn_login_click(self, login, senha):
        if verifica_login(login, senha):
            MainWindow()
            self.destroy()
        else:
            messagebox.showinfo('', f'Login {login} e/ou senha incorretos')
