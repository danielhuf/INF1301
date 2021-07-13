# Bruno Abtibol Ramos
# Daniel Stulberg Huf
# João Pedro Khair Cunha

from tkinter import *
from model import regras
from view import tabuleiro

# funções públicas do módulo
__all__ = ['click1', 'click2', 'click3', 'fimRodada']

#As três funções abaixo abrem uma nova menu de novo jogo a partir do botão de dificuldade escolhido
def click1(event):
    regras.novoJogo(1)
    tabuleiro.desenha()

def click2(event):
    regras.novoJogo(2)
    tabuleiro.desenha()

def click3(event):
    regras.novoJogo(3)
    tabuleiro.desenha()

# Função que trata da análise da última rodada feita e passagem para a próxima rodada
def fimRodada(event):
    regras.compara_senha()
    comp = regras.getCompara()
    regras.alteraDict(regras.getTentativa(),comp)
    acerto = comp[0]
    tabuleiro.escondeBotao()
    tabuleiro.preencheResp(comp, regras.getRodada())
    if (acerto == regras.getPedras()):
        tabuleiro.mostraFinal(1)     # Caso de vitória
    elif (regras.getRodada()+1 == regras.getJogadas()):
        tabuleiro.mostraFinal(0)     # Caso de derrota
    else:
        regras.novaRodada()            # Caso de prosseguimento do jogo

