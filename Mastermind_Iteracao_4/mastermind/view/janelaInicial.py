# Bruno Abtibol Ramos
# Daniel Stulberg Huf
# João Pedro Khair Cunha

from tkinter import *
from controller import eventos
from controller import historico

__all__ = ['inicia', 'mostraInexistente']

def inicia(menu):
    menu.title('Mastermind Menu')
    menu.geometry('820x520')
    menu.config(bg = 'LightCyan2')

    intro = Label(menu, bg = 'LightCyan2', text='Bem-vindo ao Mastermind!', font='Terminal 24', height=5)
    intro.pack()

    author = Label(menu, bg = 'LightCyan2', fg = 'blue', text='Criado por: Abtibol, Cunha e Huf', font='Terminal 11')
    author.place(relx=0.0, rely=1.0, anchor=SW)

    txtNivel = Label(menu, bg = 'LightCyan2', text='Escolha o nível de dificuldade', font='Terminal 15', height=5)
    b1 = Button(menu, bg = 'gold', fg = 'white', text = '1', bd = 5, font = 'Terminal', height = 2, width = 3)
    b2 = Button(menu, bg = 'blue', fg = 'white', text = '2', bd = 5, font = 'Terminal', height = 2, width = 3)
    b3 = Button(menu, bg = 'brown1', fg = 'white', text = '3', bd = 5, font = 'Terminal', height = 2, width = 3)
    volta = Button(menu, bg = 'chartreuse2', text = 'Voltar', bd = 5, font = 'Terminal', height = 2, width = 20)
    novo = Button(menu, bg = 'chartreuse2', text = 'Novo Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)

    b1.bind('<Button-1>', eventos.click1)
    b2.bind('<Button-1>', eventos.click2)
    b3.bind('<Button-1>', eventos.click3)
    volta.bind('<Button-1>', lambda event: voltaMenu(event, novo, b1, b2, b3, txtNivel))
    novo.bind('<Button-1>', lambda event: escolha_nivel(event, b1, b2, b3, volta, txtNivel))
    
    apareceNovoJogo(novo)

    retoma = Button(menu, bg = 'chartreuse2', text = 'Retomar Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)
    retoma.bind('<Button-1>', lambda event: historico.carregaJogo(event, menu))
    retoma.place(relx=0.5, rely=0.75, anchor=CENTER)

def apareceNovoJogo(novo):
    novo.place(relx=0.5, rely=0.55, anchor=CENTER)

# Desenho da parte referente à escolha do nível dentro do menu
def escolha_nivel(event, b1, b2, b3, volta, txtNivel):
    event.widget.place_forget()
    
    txtNivel.pack()
    b1.place(relx=0.38, rely=0.5, anchor=CENTER)
    b2.place(relx=0.5, rely=0.5, anchor=CENTER)
    b3.place(relx=0.62, rely=0.5, anchor=CENTER)
    volta.place(relx=0.5, rely=0.63, anchor=CENTER)

def voltaMenu(event, novo, b1, b2, b3, txtNivel):
    event.widget.place_forget()
    b1.place_forget()
    b2.place_forget()
    b3.place_forget()
    txtNivel.pack_forget()
    apareceNovoJogo(novo)

def mostraInexistente(menu):
    aviso = Label(menu, bg='LightCyan2', fg='red', text='Você não possui nenhum jogo salvo.\nInicie um novo jogo.', font='Terminal 12', height=3)
    aviso.place(relx=0.5, rely=0.85, anchor=CENTER)
    menu.after(2000, aviso.destroy)
