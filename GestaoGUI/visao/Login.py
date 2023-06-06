import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox


class Login:
    def __init__(self):
        pass

    def btn_login_click(self, login, senha):
        messagebox.showinfo('Título', f'Login: {login}, Senha: {senha}')

    def main_window(self):
        """ The window with the darkstyle """
        root = tk.Tk()
        root.title("Gestão de Automóveis - Login")
        root.resizable(True, True)
        root.geometry("600x200")
        root.iconbitmap(r'.\\img\\icone.ico')

        pady = 15
        font = 'Helvetica'

        frame_authorization = ttk.Frame(root)

        login_label = ttk.Label(
            frame_authorization,
            text="Login",
            font=(font, 12)
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
            font=(font, 12)
        )

        password_entry = ttk.Entry(
            frame_authorization,
            show="●",
            width=20,
            foreground='#666699',
            justify="center",
        )
        password_entry.insert(0, 'Min 6 characters')

        login_label.grid(row=0, column=0, padx=10, pady=pady)
        login_entry.grid(row=0, column=1, padx=10, pady=pady)
        password_label.grid(row=1, column=0, padx=10, pady=pady)
        password_entry.grid(row=1, column=1, padx=10, pady=pady)

        frame_authorization.pack()

        button = ttk.Button(
            root,
            text="Login",
            width=20,
            style='my.TButton',
            command=lambda : self.btn_login_click(login_entry.get(), password_entry.get())
        )

        button.pack(pady=pady)

        root.mainloop()
