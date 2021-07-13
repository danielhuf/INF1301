from tkinter import *
from model import regras

# Função que trata do clique das pedras para preencher cada tentativa
def onclick(event):
    global saved_color, item_ant, cnv, b_cores, ltotal, contaPreenchidos
    item = cnv.find_closest(event.x, event.y)
    if item[0] in b_cores:
        saved_color = cnv.itemcget(item, 'fill')
        if cnv.itemcget(item,'outline') == 'black':
            cnv.itemconfig(item, outline='white')
        else:
            cnv.itemconfig(item, outline='black')
        if cnv.itemcget(item,'fill')!= cnv.itemcget(item_ant,'fill'):
            cnv.itemconfig(item_ant, outline='black')
        item_ant = item
    elif item[0] in ltotal[regras.getRodada()]:
        cnv.itemconfig(item_ant, outline='black')
        cnv.itemconfig(item, fill=saved_color)
        saved_color = 'gray63'

def desenha():
    global saved_color, item_ant, cnv, b_cores, ltotal, contaPreenchidos
    # Captura dos dados necessários para criar a tabela do jogo
    cores = regras.getCores()          
    nRod = regras.getJogadas()
    nPed = regras.getPedras()

    # Criação da janela raiz
    root = Tk()
    cnv = Canvas(root, bg = 'LightCyan2', height=650, width=800)
    cnv.pack()
    root.title('Mastermind')
    menubar = Menu(root, tearoff=0)
    menubar.add_command(label='Salvar')
    menubar.add_command(label='Ajuda')
    root.config(menu=menubar)

    # Estabelecendo as 4 coordenadas base para criação da tabela
    r = 20                        # Raio de cada pedra
    Xsenha = nPed*2*(r+3) + 8*r  
    Ysenha = (nPed+1)*4*(r+3)-r  
    Xini = 400 - Xsenha/2    
    Yini = 325 - (Ysenha+3)/2

    cnv.create_rectangle(Xini, Yini-3, Xini+Xsenha, Yini+Ysenha, fill = 'gray93')

    # Desenha tentativas
    ltotal = []
    color = 'gray63'
    y = Yini + r + 3
    for tentativa in range(nRod):
        ltentativa = []
        x = Xini + 5*r + 1
        for bola in range(nPed):
            c = cnv.create_oval(x - r, y - r, x + r, y + r, fill = color)
            ltentativa.append(c)
            x += 2*(r + 3)
        ltotal.append(ltentativa)
        y += 2*(r + 3)

    # Desenha senha (abaixo da matriz de tentativas)
    x = Xini + 5*r + 1
    y += r
    for i in range(nPed):
        cnv.create_oval(x - r, y - r, x + r, y + r, fill = color)
        x += 2*(r + 3)

    # Desenha cores (posição vertical: centralizado em relação às tentativas)
    x = Xini + 2*r
    y = Yini + (nPed-1)*(r+3)
    b_cores = []
    for cor in cores:
        b_cor = cnv.create_oval(x - r, y - r, x + r, y + r, fill = cor)
        b_cores.append(b_cor)
        y += 2*(r+3)

    # Desenha avaliações de tentativa
    r2 = 6
    y = Yini + r2 + 8
    for i in range(nRod):
        x = Xini + nPed*2*(r+3) + 4*r + (r2 + 12)
        cont = 0
        for i in range(nPed):
            if cont == 3:
                x = Xini + nPed*2*(r+3) + 4*r + (r2 + 12)
                y += 2*r2 + 6
                cont = 0
            cnv.create_oval(x - r2, y - r2, x + r2, y + r2, fill = 'gray63')
            x += 2*(r2 + 4)
            cont += 1
        y += 2*(r2 + 8)

    contaPreenchidos = 0
    saved_color = 'gray63'
    item_ant = 0
    cnv.bind('<Button-1>', onclick) 
    root.mainloop()
