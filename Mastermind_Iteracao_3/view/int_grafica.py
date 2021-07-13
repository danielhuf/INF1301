# Autores: Bruno Abtibol Ramos, Daniel Stulberg Huf, João Pedro Khair Cunha

from tkinter import *
from model import regras
from controller import eventos

# funções públicas do módulo
__all__ = ['inicia', 'exibeMenu', 'desenha', 'preenche', 'cancelaEscolha', 'escondeTutorial', 'preencheResp', 'mostraSenha']

flag = 'desligado'    # situação do botão de validação da tentativa

# Design do menu inicial do jogo
def inicia(menu):
    menu.title('Mastermind Menu')
    menu.geometry('820x520')
    menu.config(bg = 'LightCyan2')

    intro = Label(menu, bg = 'LightCyan2', text='Bem-vindo ao Mastermind!', font='Terminal 24', height=5)
    intro.pack()

    author = Label(menu, bg = 'LightCyan2', fg = 'blue', text='Criado por: Abtibol, Cunha e Huf', font='Terminal 11')
    author.place(relx=0.0, rely=1.0, anchor=SW)

    novo = Button(menu, bg = 'chartreuse2', text = 'Novo Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)
    novo.bind('<Button-1>', lambda event: eventos.escolha_nivel(event, menu))
    novo.place(relx=0.5, rely=0.45, anchor=CENTER)

    retoma = Button(menu, bg = 'chartreuse2', text = 'Retomar Jogo', bd = 5, font = 'Terminal', height = 2, width = 20)
    retoma.place(relx=0.5, rely=0.7, anchor=CENTER)

# Design da parte referente à escolha do nível dentro do menu
def exibeMenu(menu):
    txtNivel = Label(menu, bg = 'LightCyan2', text='Escolha o nível de dificuldade', font='Terminal 15', height=5)
    txtNivel.pack()

    b1 = Button(menu, bg = 'gold', fg = 'white', text = '1', bd = 5, font = 'Terminal', height = 2, width = 2)
    b2 = Button(menu, bg = 'blue', fg = 'white', text = '2', bd = 5, font = 'Terminal', height = 2, width = 2)
    b3 = Button(menu, bg = 'brown1', fg = 'white', text = '3', bd = 5, font = 'Terminal', height = 2, width = 2)

    b1.place(relx=0.4, rely=0.5, anchor=CENTER)
    b2.place(relx=0.5, rely=0.5, anchor=CENTER)
    b3.place(relx=0.6, rely=0.5, anchor=CENTER)

    b1.bind('<Button-1>', eventos.click1)
    b2.bind('<Button-1>', eventos.click2)
    b3.bind('<Button-1>', eventos.click3)

# Design do tabuleiro do jogo
def desenha():
    global saved_color, item_ant, b_cores, ltotal, cnv, lcompara, tampa
    
    # Captura dos dados necessários para criar o tabuleiro do jogo
    cores = regras.getCores()          
    nRod = regras.getJogadas()
    nPed = regras.getPedras()

    # Criação da janela raiz
    root = Tk()
    cnv = Canvas(root, bg = 'LightCyan2', height=700, width=800)
    cnv.pack()
    root.title('Mastermind')
    menubar = Menu(root, tearoff=0)
    menubar.add_command(label='Salvar')
    menubar.add_command(label='Ajuda', command = exibeTutorial)
    root.config(menu=menubar)

    # Estabelecendo as 4 coordenadas base para criação do tabuleiro
    r = 20                        # Raio de cada pedra
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

    # Desenha senha (abaixo da matriz de tentativas)
    x = Xini + 5*r + 1
    y += r
    senha = regras.getSenha()
    for i in range(nPed):
        cnv.create_oval(x - r, y - r, x + r, y + r, fill = senha[i])
        x += 2*(r + 3)
    tampa = cnv.create_rectangle(Xini + 4*r + 1, y - 1.5*r, x + r - 2*(r + 3), y + r, fill = color)

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
    cnv.bind('<Button-1>', eventos.clickPedras)
    cnv.bind('<Button-2>', eventos.cancelaEsc) # MUDAR PARA ESCAPE
    root.mainloop()

# Função para exibição do tutorial
def exibeTutorial():
    global cnv, ok, box, tut
    txt = """
    -> O objetivo do Mastermind é descobrir uma combinação de cores determinada aleatoriamente pelo computador.

    -> Em cada jogada, o jogador apresenta uma combinação de pedras coloridas a que o computador responde,
    mostrando uma marca preta por cada pedra colorida na posição correta e uma marca branca por cada pedra
    colorida presente na combinação, mas em uma outra posição que não seja a correta.

    -> Pela resposta do computador, o jogador apresenta uma nova combinação, juntando
    cores que ainda não foram escolhidas, ou trocando a ordem das cores, ou ambos.

    -> O jogo progride até que a combinação seja descoberta ou que o número limite de jogadas seja atingido.

    -> Esta implementação do Mastermind oferece três níveis de dificuldade crescente. Do nível I ao nível III cresce
    o número de pedras da chave, o número de cores a considerar e o número de jogadas disponíveis para descobrir a chave.
    
    """
    box = cnv.create_rectangle(5,5,797,260, fill='gray93')
    tut = cnv.create_text(400, 120, fill='blue', text=txt, anchor=CENTER, justify=CENTER)
    ok = Button(cnv, text = 'Ok', bd = 5, height = 1, width = 10)
    ok.bind('<Button-1>', eventos.clicaOk)
    ok.place(relx=0.5, rely=0.35, anchor=CENTER)

# Tratamento da escolha das pedras para cada tentativa e do posicionamento da pedra escolhida dentro do tabuleiro
def preenche(cnv,item):
    global saved_color, item_ant, b_cores, ltotal, lcompara
    tentativa = regras.getTentativa()
    numRodadas = regras.getRodada()
    
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
        
    elif item[0] in ltotal[regras.getRodada()]:
        cnv.itemconfig(item_ant, outline='black')
        cnv.itemconfig(item, fill=saved_color)
        tentativa[ltotal[numRodadas].index(item[0])] = saved_color
        regras.alteraTentativa(tentativa)
        verifica(tentativa, cnv)
        saved_color = 'gray63'

# Função que interrompe a seleção da cor
def cancelaEscolha():
    global saved_color, item_ant, cnv
    saved_color = 'gray63'
    cnv.itemconfig(item_ant, outline='black')

# Função para esconder o botão de validação da tentativa
def escondeBotao():
    global flag, valida
    valida.place_forget()
    flag = 'desligado'

def escondeTutorial():
    global cnv, ok, box, tut
    cnv.delete(tut)
    cnv.delete(box)
    ok.place_forget()

# Verificação das condições para o aparecimento/desaparecimento do botão de validação da tentativa
def verifica(tentativa, cnv):
    global flag, valida
    
    if '' not in tentativa and 'gray63' not in tentativa and flag == 'desligado':
        valida = Button(cnv, bg = 'chartreuse2', text = 'Validar tentativa?', bd = 5, font = 'Terminal', height = 2, width = 20)
        valida.bind('<Button-1>', eventos.fimRodada)
        dif = regras.getPedras()-3
        if dif==1:
            valida.place(relx=0.5, rely=0.1, anchor=CENTER)
        elif dif==2:
            valida.place(relx=0.5, rely=0.042, anchor=CENTER)
        else:
            valida.place(relx=0.16, rely=0.05, anchor=CENTER)
        flag = 'ligado'
        
    elif tentativa.count('gray63') == 1 and flag == 'ligado':
        escondeBotao()
        
# Preenchimento dos pinos de comparação entre a tentativa e a senha
def preencheResp(compara):
    global saved_color, item_ant, b_cores, ltotal, cnv, lcompara
    nRod = regras.getRodada()
    acerto = 0
    for el in lcompara[nRod]:
        if compara[0]!=0:
            cnv.itemconfig(el, fill='black')
            compara[0] -= 1
            acerto += 1
        elif compara[1]!=0:
            cnv.itemconfig(el, fill='white')
            compara[1] -= 1
    escondeBotao()
    return acerto

# Função que retira o retângulo tampando a senha
def mostraSenha():
    global cnv, tampa
    cnv.delete(tampa)
    
    
    
        
    
    
