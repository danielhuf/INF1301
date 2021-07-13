# Autores: Bruno Abtibol Ramos, Daniel Stulberg Huf, João Pedro Khair Cunha

import random

# funções públicas do módulo
__all__ = ['novoJogo', 'alteraTentativa', 'novaRodada', 'compara_senha', 'getCores', 'getJogadas',
           'getPedras', 'getSenha', 'getRodada', 'getTentativa', 'getCompara'] 

def novoJogo(dif):
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        rodada = 0                                             # número de rodadas do jogo, inicializado em 0
        (nPedras, cores, nJogadas) = escolhe_nivel(dif)        # número de pedras, lista de cores e numero de jogadas são determinados de acordo com o nível 
        senha = define_senha()                                 # lista com a senha é definida, ela será posteriormente preenchida com uma lista de cores
        tentativa = []                                         # uma tentativa é inicializada como uma lista vazia, ela será posteriormente preenchida com uma lista de cores
        for i in range(nPedras):
                tentativa.append('')                           # lista da tentativa é inicilizada com n vazios, sendo n o número de pedras
        compara = [0,0]                                        # lista do compara é inicializada contendo os resultados de cada jogada:
                                                               # compara: posição 0 -> número de pinos pretos
                                                               # compara: posição 1 -> número de pinos brancos

def escolhe_nivel(dif):
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        niveis = [[4, 6, 8], [5, 7, 10], [6, 8, 12]]                                                    # lista com as características do jogo em cada nível
        cores_totais = ['red', 'green', 'blue', 'yellow', 'pink', 'cyan', 'dark goldenrod', 'purple3']  # lista de todas as cores presentes no jogo
        nivel = niveis[dif-1]
        cores_nivel = cores_totais[0:nivel[1]]                                                          # cores específicas para o nível escolhido são selecionadas
        return (nivel[0], cores_nivel, nivel[2])                                                        # características do jogo para o nível escolhido são retornadas


def define_senha():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        senha = []
        for i in range(nPedras):
                senha.append(random.choice(cores))                         # senha é definida de forma aleatória a partir do número de pedras e as cores específicas do nível escolhido
        return senha

def alteraTentativa(tent):
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        tentativa = tent

def novaRodada():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        rodada += 1
        tentativa = []
        for i in range(nPedras):
                tentativa.append('')                                       # lista da tentativa é reinicializada       

def compara_senha():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        aux_senha = senha.copy()                                           # cópias das listas com a senha e tentativa são criadas para serem manipuladas durante a comparação dos resultados da rodada                    
        aux_tentativa = tentativa.copy()
                
        for i in range(nPedras):                                           # iterando n vezes, n = número de pedras do nível, compara-se apenas as cores acertadas nas posições corretas, incrementando o número de pinos pretos
                if aux_tentativa[i] == aux_senha[i]:
                        compara[0] += 1
                        aux_tentativa[i] = 'done_tent'
                        aux_senha[i] = 'done_senha'
        
        for i in range(nPedras):                                           # iterando n vezes, n = número de pedras do nível, compara-se agora as cores acertadas, mas em uma posição diferente da correta, incrementando o número de pinos brancos                               
                if aux_tentativa[i] in aux_senha:
                        compara[1] += 1
                        for j in range(len(aux_senha)):                    # caso um pino branco seja incrementado, trocamos a pedra correspondente de aux_senha para 'done_senha', para que ela não seja comparada a outras pedras da mesma cor mas em outra posição
                                if aux_senha[j] == aux_tentativa[i]:
                                        aux_senha[j] = 'done_senha'
                                        break

# Abaixo, são definidas as funções que retornam as variáveis globais

def getCores():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return cores

def getJogadas():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return nJogadas

def getPedras():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return nPedras

def getSenha():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return senha

def getRodada():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return rodada

def getTentativa():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return tentativa

def getCompara():
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara
        return compara

