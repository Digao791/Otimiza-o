import controle as co
import numpy as np
import Maximize
import Minimize

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

if co.opcao == "Maximize":
    matriz = Maximize.retornar_matriz()
elif co.opcao == "Minimize":
    matriz = Minimize.retornar_matriz()

np.set_printoptions(precision=2, suppress=True)
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


co.lucro_maximo = matriz[0,-1]
lucro = co.lucro_maximo
co.preco_sombra = matriz[0, co.nConstantes:-1]
pSombra = co.preco_sombra
co.melhor_pontos = matriz[1:, -1]
mPontos = co.melhor_pontos

print(lucro)
print(pSombra)
print(mPontos)
print(matriz)