from model import regras

#Inicializa as variáveis globais para testar as funções de dentro.
#Só pra não ter q inicializar cada uma manualmente, mas o certo é testar as de dentro antes 
regras.novoJogo()

#Teste unitário 1
def escolhe_nivel():
        niveis = [[4, 6, 8], [5, 7, 10], [6, 8, 12]]
        cores_totais = ['red', 'green', 'blue', 'yellow', 'pink', 'cyan', 'brown', 'purple']
        escolha = int(input('Saudações jogador! Qual nível você deseja jogar? (1/2/3)\n'))
        nivel = niveis[escolha-1]
        cores_nivel = cores_totais[0:nivel[1]]
        return (nivel[0], cores_nivel, nivel[2]) #(nPedras, cores, nRodadas)

l = escolhe_nivel()
print('N° de pedras:',l[0])
print('Lista de cores:',l[1])
print('N° de jogadas:',l[2])
print()


#Teste unitário 2

print('Senha aleatória:',regras.define_senha())
print()
print('Senha aleatória:',regras.define_senha())

print()


#Teste unitário 3
regras.novoJogo()
print('Lista de cores:', regras.getCores())
print('N° de jogadas:', regras.getJogadas())
print('N° de pedras:', regras.getPedras())
print('Senha aleatória:', regras.getSenha())
print('N° da rodada atual:', regras.getRodada())
print('Tentativa de senha:', regras.getTentativa())
l = regras.getCompara()
print('N° de pretas:',l[0])
print('N° de brancas:',l[1])
print('N° de vazios:',l[2])


#Teste unitário 4
nPedras = regras.getPedras()
def compara_senha(nPedras):
        senha = regras.define_senha()
        tentativa = regras.define_senha()
        aux_senha = senha.copy()                         
        aux_tentativa = tentativa.copy()
        print('Senha:',senha)
        print('Tentativa:',tentativa)
        compara = [0,0,0]
                
        for i in range(nPedras):
                if aux_tentativa[i] == aux_senha[i]:
                        compara[0] += 1
                        aux_tentativa[i] = 'done_tent'
                        aux_senha[i] = 'done_senha'
                
        for i in range(nPedras):
                if aux_tentativa[i] in aux_senha:
                        compara[1] += 1
                        for j in range(len(aux_senha)):
                                if aux_senha[j] == aux_tentativa[i]:
                                        aux_senha[j] = 'done_senha'
                                        break
                compara[2] = nPedras - (compara[0] + compara[1])
        return compara
for i in range(5):    
    l = compara_senha(nPedras)
    print('N° de pretas:',l[0])
    print('N° de brancas:',l[1])
    print('N° de vazios:',l[2],'\n')
