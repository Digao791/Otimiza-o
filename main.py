import controle as co
import re
import numpy as np

#! Primeiro passo -> Extrair as informações dos textos

# *Colhendo os coeficientes da função Z
coeficientes = re.findall(r'[-+]?\d*\.?\d+', co.funcao)
coeficientes = [float(numero) for numero in coeficientes]
coeficientes = [ -numero for numero in coeficientes]


linha_z = coeficientes + ([0.0] * len(co.restricoes) + [0])
# *Colhendo os coeficientes das restrições
restricoes = []
index = 0
for restricao in co.restricoes:
    values = re.findall(r'[-+]?\d*\.?\d+', restricao[0])
    values = [float(numero) for numero in values]
    variaveis = [0.0]*len(co.restricoes)
    variaveis[index] = 1.0 if restricao[1] == "<=" else -1.0
    index+=1
    ld = [restricao[2]]
    restricoes.append(values + variaveis + ld)

#Criando a matriz principal
linhas = [linha_z] + [linha for linha in restricoes]

matriz = np.zeros(shape=(len(co.restricoes) + 1,len(coeficientes) + len(co.restricoes)))
matriz = np.vstack(linhas)
matriz = matriz.astype(float)
np.set_printoptions(precision=2, suppress=True)


def encontrar_coluna_pivo(linha):
    return np.argmin(linha)
    
def encontrar_linha_pivo(coluna):
    menor = np.inf
    i = 0
    linha = 1
    for i in range(len(coluna)):
        if float(matriz[i+1,-1])/float(coluna[i]) < menor:
            menor = float(matriz[i+1,-1])/float(coluna[i])
            linha = i + 1
    variaveis_base.append(linha)
    return linha

def encontrar_elemento_pivo(linha_z):
    coluna_pivo = encontrar_coluna_pivo(linha_z)
    linha_pivo  = encontrar_linha_pivo(matriz[1:, coluna_pivo])

    return [float(matriz[linha_pivo, coluna_pivo]), linha_pivo, coluna_pivo]

def atualizar_linha_referencia(linha, elemento_pivo):
    matriz[linha,:] = matriz[linha,:]/elemento_pivo
    
def atualizar_restante_da_matriz(linha, coluna):
    for i in range((len(co.restricoes)) + 1):
        if i == linha:
            continue
        matriz[i] = matriz[i] -1*(matriz[i, coluna])*matriz[linha]

linha_z = matriz[0].astype(float)
valores = linha_z[np.where(linha_z < 0)]
variaveis_base = []

while(len(valores) > 0):

    print(matriz)

    elemento_pivo = encontrar_elemento_pivo(linha_z)
    print(elemento_pivo)
    atualizar_linha_referencia(elemento_pivo[1], elemento_pivo[0])
    atualizar_restante_da_matriz(elemento_pivo[1], elemento_pivo[2])
    
    linha_z = matriz[0].astype(float)
    valores = linha_z[np.where(linha_z < 0)]

    x = input()

print(matriz)
co.lucro_maximo = str(matriz[0,-1])
co.preco_sombra = str(matriz[0, len(coeficientes) : -1])


print("Melhor lucro: " + str(matriz[0, -1]))
print("Preço sombra: " + str(matriz[0, len(coeficientes) : -1]))
print("Ponto ótimo de operação: " + str(matriz[1:,-1]))