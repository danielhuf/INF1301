# Bruno Abtibol Ramos
# Daniel Stulberg Huf
# João Pedro Khair Cunha

import random

# funções públicas do módulo
__all__ = ['novoJogo', 'alteraTentativa', 'novaRodada', 'compara_senha', 'getCores', 'getJogadas',
           'getPedras', 'getSenha', 'getRodada', 'getTentativa', 'getCompara', 'getDificuldade', 'getDict'] 

def novoJogo(dif):
        global cores, nJogadas, nPedras, senha, rodada, tentativa, compara, dificuldade, dict_saved, dict_saved, dict_saved
        rodada = 0
        dificuldade = dif
        (nPedras, cores, nJogadas) = escolhe_nivel(dif)
        senha = define_senha()
        tentativa = []
        for i in range(nPedras):
                tentativa.append('gray63')      # cor correspondente a espaço vazio
        compara = [0,0]                         # lista: [número de pinos pretos, número de pinos brancos]
        dict_saved = {}                         # {'T':[lista de listas tentativa], 'C': [lista de listas compara]}
                                                               

def escolhe_nivel(dif):
        niveis = [[4, 6, 8], [5, 7, 10], [6, 8, 12]]                                                    # lista com as características do jogo em cada nível
        cores_totais = ['red', 'green', 'blue', 'yellow', 'pink', 'cyan', 'darkgoldenrod', 'purple3']   # lista de todas as cores presentes no jogo
        nivel = niveis[dif-1]
        cores_nivel = cores_totais[0:nivel[1]]                                                          # cores específicas para o nível escolhido são selecionadas
        return (nivel[0], cores_nivel, nivel[2])                                                        # características do jogo para o nível escolhido são retornadas


def define_senha():
        global nPedras, senha
        senha = []
        for i in range(nPedras):
                senha.append(random.choice(cores))                         # senha é definida de forma aleatória a partir do número de pedras e as cores específicas do nível escolhido
        return senha

def alteraTentativa(saved_tent):
        global tentativa
        tentativa = saved_tent

def alteraSenha(saved_senha):
        global senha
        senha = saved_senha

def alteraRodada(saved_rodada):
        global rodada
        rodada = saved_rodada

def alteraDict(tent = 0,comp = 0):
        global dict_saved
        if tent != 0:
                tents = dict_saved.get('T',[])
                tents.append(tent)
                dict_saved['T'] = tents
        if comp != 0:
                comp = [str(i) for i in comp]
                comps = dict_saved.get('C',[])
                comps.append(comp)
                dict_saved['C'] = comps
        

def novaRodada():
        global nPedras, rodada, tentativa
        rodada += 1
        tentativa = []
        for i in range(nPedras):
                tentativa.append('gray63')      # lista da tentativa é reinicializada    

def compara_senha():
        global nPedras, senha, tentativa, compara
        aux_senha = senha.copy()                        # cópias das listas com a senha e tentativa são criadas para serem manipuladas durante a comparação dos resultados da rodada                    
        aux_tentativa = tentativa.copy()
                
        for i in range(nPedras):                        # iterando n vezes, n = número de pedras do nível, compara-se apenas as cores acertadas nas posições corretas, incrementando o número de pinos pretos
                if aux_tentativa[i] == aux_senha[i]:
                        compara[0] += 1
                        aux_tentativa[i] = 'done_tent'
                        aux_senha[i] = 'done_senha'
        
        for i in range(nPedras):                        # iterando n vezes, n = número de pedras do nível, compara-se agora as cores acertadas, mas em uma posição diferente da correta, incrementando o número de pinos brancos                               
                if aux_tentativa[i] in aux_senha:
                        compara[1] += 1
                        for j in range(len(aux_senha)): # caso um pino branco seja incrementado, trocamos a pedra correspondente de aux_senha para 'done_senha', para que ela não seja comparada a outras pedras da mesma cor mas em outra posição
                                if aux_senha[j] == aux_tentativa[i]:
                                        aux_senha[j] = 'done_senha'
                                        break

# Abaixo, são definidas as funções que retornam as variáveis globais

def getCores():
        global cores
        return cores

def getJogadas():
        global nJogadas
        return nJogadas

def getPedras():
        global nPedras
        return nPedras

def getSenha():
        global senha
        return senha

def getRodada():
        global rodada
        return rodada

def getTentativa():
        global tentativa
        return tentativa

def getCompara():
        global compara
        return compara

def getDificuldade():
        global dificuldade
        return dificuldade

def getDict():
        global dict_saved
        return dict_saved

