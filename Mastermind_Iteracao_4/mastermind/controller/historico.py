# Bruno Abtibol Ramos
# Daniel Stulberg Huf
# João Pedro Khair Cunha

from os import path
from model import regras
from view import janelaInicial
from view import tabuleiro

# funções públicas do módulo
__all__ = ['salvaJogo', 'carregaJogo']

def salvaJogo():
    f = open("jogo_salvo.txt","w")
    dif = regras.getDificuldade()
    f.write(str(dif))
    f.write('\n')
    n = regras.getRodada()
    f.write(str(n))
    f.write('\n')
    
    senha = regras.getSenha()
    s=''
    # Gravar a senha no arquivo: el1 el2 el3 el4 ...
    for el in senha:
        s += f'{el} '
    s = s[:-1] + '\n'
    f.write(s)

    # Gravar a tentativa atual no arquivo: el1 el2 el3 el4 ...
    tent = regras.getTentativa()
    s=''
    for el in tent:
        s += f'{el} '
    s = s[:-1] + '\n' #Retirar espaço final e concluir string
    f.write(s)

    if n>0:
        d = regras.getDict()
        for el in d['T']: #Grava lista de tentativas, cada uma em uma linha: x1 x2 x3 x4 ...
            s=''
            for x in el:
                s += f'{x} '
            s = s[:-1] + '\n'
            f.write(s)
        for el in d['C']: #Grava lista de comparações, cada uma em uma linha: x1 x2 x3 x4 ...
            s=''
            for x in el:
                s += f'{x} '
            s = s[:-1] + '\n'
            f.write(s)
    f.close()

def carregaJogo(event, menu):
    if(path.isfile("jogo_salvo.txt")):
        f = open("jogo_salvo.txt", "r")
        #Inicializa o jogo e atualiza os valores das estruturas com base no arquivo
        dif = int(f.readline().strip())
        nRod = int(f.readline().strip())
        saved_senha = f.readline().strip().split(' ')
        saved_tent = f.readline().strip().split(' ')
        ltents = []
        lcomps = []
        regras.novoJogo(dif)
        regras.alteraSenha(saved_senha)
        regras.alteraTentativa(saved_tent)
        regras.alteraRodada(nRod)
        
        if nRod>0: #Sem rodadas prévias completas
            for i in range(nRod): #Salvar tentativas anteriores
                l = f.readline().strip().split(' ')
                ltents.append(l)
                regras.alteraDict(tent = l)
                
            for i in range(nRod): #Salvar comparações anteriores
                l = f.readline().strip().split(' ')
                l = [int(j) for j in l]
                lcomps.append(l)
                regras.alteraDict(comp = l)
                
        tabuleiro.carregaTabuleiro(ltents, lcomps)
        f.close()
    else:   #caso não haja nenhum arquivo previamente salvo
        janelaInicial.mostraInexistente(menu)
