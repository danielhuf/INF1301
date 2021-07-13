# Autores: Bruno Abtibol Ramos, Daniel Stulberg Huf, João Pedro Khair Cunha

from tkinter import *
from model import regras
from view import int_grafica

# funções públicas do módulo
__all__ = ['click1', 'click2', 'click3', 'escolha_nivel', 'clickPedras', 'cancelaEsc', 'clicaOk', 'fimRodada']

#As três funções abaixo abrem uma nova menu de novo jogo a partir do botão de dificuldade escolhido
def click1(event):
    regras.novoJogo(1)
    int_grafica.desenha()

def click2(event):
    regras.novoJogo(2)
    int_grafica.desenha()

def click3(event):
    regras.novoJogo(3)
    int_grafica.desenha()

#Criação dos botões de dificuldade do menu principal
def escolha_nivel(event, menu):
    event.widget.place_forget()
    int_grafica.exibeMenu(menu)

# Função que trata do clique das pedras para preencher cada tentativa
def clickPedras(event):
    item = event.widget.find_closest(event.x, event.y)
    int_grafica.preenche(event.widget, item)

# Função que trata do clique no botão Esc, para interromper a seleção da cor
def cancelaEsc(event):
    int_grafica.cancelaEscolha()

# Função que trata do clique do Ok do tutorial
def clicaOk(event):
    int_grafica.escondeTutorial()

# Função que trata da análise da última rodada feita e passagem para a próxima rodada
def fimRodada(event):
    regras.compara_senha()
    comp = regras.getCompara()
    acerto = int_grafica.preencheResp(comp)
    if(acerto == regras.getPedras()):
        print('ganhou!')
        int_grafica.mostraSenha()
        #int_grafica.fimJogo()
    regras.novaRodada()

