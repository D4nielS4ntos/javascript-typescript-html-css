import tkinter as tk
from tkinter import messagebox

def mostrar_mensagem():
    messagebox.showinfo("O Jogo", "Você perdeu o jogo")

root = tk.Tk()
root.withdraw()  # Esconde a janela principal
mostrar_mensagem()
