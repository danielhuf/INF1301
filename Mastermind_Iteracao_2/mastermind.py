from tkinter import *      #posso deixar assim? ou preciso fazer 'import tkinter'?
from model import regras
from view import int_grafica

def click1(event):
    regras.novoJogo(1)
    int_grafica.desenha()

def click2(event):
    regras.novoJogo(2)
    int_grafica.desenha()

def click3(event):
    regras.novoJogo(3)
    int_grafica.desenha()

#Criação dos botões de dificuldade da janela principal
def escolha_nivel(event):
    event.widget.place_forget()
    Label(root, bg = 'LightCyan2', text='Escolha o nível de dificuldade', font='Terminal 15', height=5).pack()

    b1 = Button(root, bg = 'gold', fg = 'white', text = '1', bd = 5, font = 'Terminal', height = 2, width = 2)
    b2 = Button(root, bg = 'blue', fg = 'white', text = '2', bd = 5, font = 'Terminal', height = 2, width = 2)
    b3 = Button(root, bg = 'brown1', fg = 'white', text = '3', bd = 5, font = 'Terminal', height = 2, width = 2)

    b1.place(relx=0.4, rely=0.5, anchor=CENTER)
    b2.place(relx=0.5, rely=0.5, anchor=CENTER)
    b3.place(relx=0.6, rely=0.5, anchor=CENTER)

    b1.bind('<Button-1>', click1)
    b2.bind('<Button-1>', click2)
    b3.bind('<Button-1>', click3)

#Criação da janela principal
root = Tk()
root.title('Mastermind Menu')
root.geometry('820x520')
root.config(bg = 'LightCyan2')

intro = Label(root, bg = 'LightCyan2', text='Bem-vindo ao Mastermind!', font='Terminal 24', height=5)
intro.pack()

author = Label(root, bg = 'LightCyan2', fg = 'blue', text='Criado por: Abtibol, Cunha e Huf', font='Terminal 11')
author.place(relx=0.0, rely=1.0, anchor=SW)

novo = Button(root, bg = 'chartreuse2', text = 'Novo Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)
novo.bind('<Button-1>', escolha_nivel)
novo.place(relx=0.5, rely=0.45, anchor=CENTER)

retoma = Button(root, bg = 'chartreuse2', text = 'Retomar Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)
retoma.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()
