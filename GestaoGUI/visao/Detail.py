import tkinter as tk
import tkinter.ttk as ttk
from tkinter import END
from GestaoGUI.persistencia.automoveis_db import *
from GestaoGUI.modelos.Automovel import Automovel

def set_text(entry_widget, text):
    entry_widget.delete(0, END)
    entry_widget.insert(0, text)


class Detail(ttk.Frame):
    def __init__(self, root):
        super().__init__(root)

        """ Constantes """
        self.pady = 15
        
        self.font = 'Helvetica'
        self.font_size = 14

        self.vehicles_list = retorna_automoveis()

        vehicles_listbox = tk.Listbox(root, width=60, selectmode='single')

        vehicles_listbox.config(font = self.font)

        for vehicle in self.vehicles_list:
            vehicles_listbox.insert(self.vehicles_list.index(vehicle) + 1, vehicle.get_nome())

        vehicles_listbox.bind('<<ListboxSelect>>', self.change_data)

        vehicles_listbox.pack(expand=True, padx=20, pady=40)

        # Configure labels & entries

        ttk.Label(self, text="Número", font=self.font).pack()
        self.entry_numero = ttk.Entry(self, width=30)
        self.entry_numero.pack(pady=3)

        ttk.Label(self, text="Nome", font=self.font).pack()
        self.entry_nome = ttk.Entry(self, width=30)
        self.entry_nome.pack(pady=3)

        ttk.Label(self, text="Marca", font=(self.font, self.font_size)).pack()
        self.entry_marca = ttk.Entry(self, width=30)
        self.entry_marca.pack(pady=3)

        ttk.Label(self, text="Ano", font=(self.font, self.font_size)).pack()
        self.entry_ano = ttk.Entry(self, width=30)
        self.entry_ano.pack(pady=3)

        ttk.Label(self, text="Cor", font=(self.font, self.font_size)).pack()
        self.entry_cor = ttk.Entry(self, width=30)
        self.entry_cor.pack(pady=3)

        ttk.Label(self, text="Alugado", font=(self.font, self.font_size)).pack()
        self.entry_alugado = ttk.Entry(self, width=30)
        self.entry_alugado.pack(pady=3)

    def change_data(self, evt):
        widget_selected = evt.widget
        index = int(widget_selected.curselection()[0])
        # value = widget_selected.get(index)
        automovel = self.vehicles_list[index]

        set_text(self.entry_numero, automovel.numero[0])
        set_text(self.entry_nome, automovel.nome[0])
        set_text(self.entry_marca, automovel.marca[0])
        set_text(self.entry_ano, automovel.ano[0])
        set_text(self.entry_cor, automovel.cor)
        set_text(self.entry_alugado, automovel.get_situacao_aluguel())
