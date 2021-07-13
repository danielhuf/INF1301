# Bruno Abtibol Ramos
# Daniel Stulberg Huf
# João Pedro Khair Cunha

from tkinter import *
from model import regras
from controller import eventos
from controller import historico

__all__ = ['desenha', 'escondeBotaao', 'preencheResp', 'mostraFinal', 'carregaTabuleiro']
    
# Desenho do tabuleiro do jogo
def desenha():
    global menubar, saved_color, item_ant, b_cores, ltotal, cnv, lcompara, tampa, txt_tampa, jogo, root, flag, valida
    jogo = 'operando'
    cores = regras.getCores()          
    nRod = regras.getJogadas()
    nPed = regras.getPedras()

    # Criação da janela raiz
    root = Tk()
    cnv = Canvas(root, bg = 'LightCyan2', height=700, width=800)
    cnv.pack()
    root.title('Mastermind')
    menubar = Menu(root, tearoff=0)
    menubar.add_command(label='Salvar', command = historico.salvaJogo)
    root.config(menu=menubar)
    valida = Button(cnv, bg = 'chartreuse2', text = 'Validar tentativa?', bd = 5, font = 'Terminal', height = 2, width = 20)
    valida.bind('<Button-1>', eventos.fimRodada)
    flag = 'desligado'    # situação do botão de validação da tentativa

    r = 20  # Raio de cada pedra
    # Estabelecendo as 4 coordenadas base para criação do tabuleiro
    Xsenha = nPed*2*(r+3) + 8*r  
    Ysenha = (nPed+1)*4*(r+3)-r  
    Xini = 400 - Xsenha/2    
    Yini = 350 - (Ysenha+3)/2
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

    # Desenha senha (abaixo da matriz de tentativas) e tampa ela
    x = Xini + 5*r + 1
    y += r
    senha = regras.getSenha()
    for i in range(nPed):
        cnv.create_oval(x - r, y - r, x + r, y + r, fill = senha[i])
        x += 2*(r + 3)
    tampa = cnv.create_rectangle(Xini + 4*r + 1, y - 1.5*r, x + r - 2*(r + 3), y + r, fill = color)
    txt_tampa = cnv.create_text(400, y - 1.5*r + 25, fill='blue', text='S E N H A', font = 'Terminal', anchor=CENTER, justify=CENTER)

    # Desenha cores (posição vertical: centralizado em relação às tentativas)
    x = Xini + 2*r
    y = Yini + (nPed-1)*(r+3)
    b_cores = []
    for cor in cores:
        b_cor = cnv.create_oval(x - r, y - r, x + r, y + r, fill = cor)
        b_cores.append(b_cor)
        y += 2*(r+3)

    # Desenha avaliações de tentativa
    lcompara = []
    r2 = 6
    y = Yini + r2 + 8
    for i in range(nRod):
        aux = []
        x = Xini + nPed*2*(r+3) + 4*r + (r2 + 12)
        cont = 0
        for i in range(nPed):
            if cont == 3:
                x = Xini + nPed*2*(r+3) + 4*r + (r2 + 12)
                y += 2*r2 + 6
                cont = 0
            c = cnv.create_oval(x - r2, y - r2, x + r2, y + r2, fill = 'gray63')
            aux.append(c)
            x += 2*(r2 + 4)
            cont += 1
        lcompara.append(aux)
        y += 2*(r2 + 8)

    saved_color = 'gray63'
    item_ant = 0
    cnv.bind('<Button-1>', preenche)
    cnv.bind_all('<Escape>', cancelaEscolha)

# Preenchimento da escolha das pedras para cada tentativa
def preenche(event):
    global cnv, saved_color, item_ant, b_cores, ltotal, lcompara, jogo
    tentativa = regras.getTentativa()
    numRodadas = regras.getRodada()

    if jogo == 'operando':
        item = event.widget.find_closest(event.x, event.y)
        # Escolha da pedra dentre as opções de cores disponíveis
        if item[0] in b_cores:
            saved_color = cnv.itemcget(item, 'fill')
            if cnv.itemcget(item,'outline') == 'black':
                cnv.itemconfig(item, outline='white')
            else:
                cnv.itemconfig(item, outline='black')
            if cnv.itemcget(item,'fill')!= cnv.itemcget(item_ant,'fill'):
                cnv.itemconfig(item_ant, outline='black')
            elif cnv.itemcget(item_ant, 'outline')=='black':
                saved_color = 'gray63'
            item_ant = item
        # Posicionamento da pedra escolhida dentro do tabuleiro
        elif item[0] in ltotal[regras.getRodada()]:
            cnv.itemconfig(item_ant, outline='black')
            cnv.itemconfig(item, fill=saved_color)
            tentativa[ltotal[numRodadas].index(item[0])] = saved_color
            regras.alteraTentativa(tentativa)
            verifica(tentativa)
            saved_color = 'gray63'

def cancelaEscolha(event):
    global saved_color, item_ant, cnv
    saved_color = 'gray63'
    cnv.itemconfig(item_ant, outline='black')

def escondeBotao():
    global flag, valida
    valida.place_forget()
    flag = 'desligado'

# Verificação das condições para o aparecimento/desaparecimento do botão de validação da tentativa
def verifica(tentativa):
    global flag, cnv, valida
    if 'gray63' not in tentativa and flag == 'desligado':
        valida = Button(cnv, bg = 'chartreuse2', text = 'Validar tentativa?', bd = 5, font = 'Terminal', height = 2, width = 20)
        valida.bind('<Button-1>', eventos.fimRodada)
        dif = regras.getDificuldade()
        if dif==1:
            valida.place(relx=0.5, rely=0.1, anchor=CENTER)
        elif dif==2:
            valida.place(relx=0.5, rely=0.042, anchor=CENTER)
        else:
            valida.place(relx=0.16, rely=0.05, anchor=CENTER)
        flag = 'ligado'
        
    elif tentativa.count('gray63') == 1 and flag == 'ligado':
        escondeBotao()
        
def preencheResp(compara, nRod):
    global cnv, lcompara
    for el in lcompara[nRod]:
        if compara[0]!=0:
            cnv.itemconfig(el, fill='black')
            compara[0] -= 1
        elif compara[1]!=0:
            cnv.itemconfig(el, fill='white')
            compara[1] -= 1

def mostraFinal(n):
    global cnv, tampa, txt_tampa, jogo, menubar
    jogo = 'finalizado'
    cnv.delete(txt_tampa)
    cnv.delete(tampa)
    menubar.delete(0, END) #Retira a opção de salvar pois o jogo acabou
    dif = regras.getDificuldade()
    if n:
        txt = 'Parabéns! Você venceu a partida de Mastermind!'
        color = 'blue'
    else:
        txt = 'Não foi dessa vez! Tente outra partida!'
        color = 'red'
    if dif==1:
        y = 90
    elif dif==2:
        y = 65
    else:
        y = 20
    cnv.create_text(400, y, fill = color, font = 'Terminal 21', text=txt, anchor=CENTER, justify=CENTER)

def carregaTabuleiro(ltents, lcomps):
    global cnv, ltotal, root
    desenha()
    nRod = regras.getRodada()
    nPed = regras.getPedras()

    #Preenche as bolas nas cores das tentativas anteriores
    if nRod>0:
        for rodada in range(nRod):
            for i in range(nPed):
                bola = ltotal[rodada][i]
                cor = ltents[rodada][i]
                cnv.itemconfig(bola, fill=cor)
            preencheResp(lcomps[rodada],rodada)#Preenche as comparações das tentativas com a senha
    tent = regras.getTentativa()
     
    #Preence as cores da tentativa atual (vazia, incompleta ou não validada)
    for i in range(nPed):
        bola = ltotal[nRod][i]
        cor = tent[i]
        cnv.itemconfig(bola, fill=cor)
    verifica(tent) #Mostra o botão de validar senha caso o salvamento permita
    root.mainloop()
