import controle as co
import numpy as np
import Maximize
import Minimize
import re

#Função retorna o menor negativo na linha Z ( Coluna Pivo )
def encontrar_coluna_pivo(linha):
    return np.argmin(linha)
    
#Função retorna a linha pivô 
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

#Encontra o elemento pivô
def encontrar_elemento_pivo(linha_z):
    coluna_pivo = encontrar_coluna_pivo(linha_z)
    linha_pivo  = encontrar_linha_pivo(matriz[1:, coluna_pivo])

    variaveis_base[coluna_pivo] = variaveis_de_base[coluna_pivo]
    
    return [float(matriz[linha_pivo, coluna_pivo]), linha_pivo, coluna_pivo]

#Função a linha de referência da matriz
def atualizar_linha_referencia(linha, elemento_pivo):
    matriz[linha,:] = matriz[linha,:]/elemento_pivo
    
#Atualiza o restante da matriz
def atualizar_restante_da_matriz(linha, coluna):
    for i in range((len(co.restricoes)) + 1):
        if i == linha:
            continue
        matriz[i] = matriz[i] -1*(matriz[i, coluna])*matriz[linha]

#Se a opção escolhida for de Maximizar, é retornado a matriz de maximizar
if co.opcao == "Maximize":
    matriz = Maximize.retornar_matriz()
#Se a opção escolhida for de Minimizar, é retornado a matriz de maximizar
elif co.opcao == "Minimize":
    matriz = Minimize.retornar_matriz()
else:
    print("Nenhuma opção escolhida")

#Define a saída para duas casas decimais
np.set_printoptions(precision=2, suppress=True)
#Armazena a primeira linha da matriz como valores float
linha_z = matriz[0].astype(float)
#Filtra pelos valores menores que zero
valores = linha_z[np.where(linha_z < 0)]
#Variáveis que se encontram na base
variaveis_base = []

variaveis_de_base = re.findall(r'[a-zA-Z]', co.funcao)
variaveis_de_base = [str(letra) for letra in variaveis_de_base]

#Enquanto tiver valores negativos na linha Z
while(len(valores) > 0):

    #Mostra a matriz atual
    print(matriz)

    #Encontra o elemento pivô
    elemento_pivo = encontrar_elemento_pivo(linha_z)
    #Apresenta o elemento pivô e suas coordenadas

    print(elemento_pivo)
    #Atualiza a linha de referência
    atualizar_linha_referencia(elemento_pivo[1], elemento_pivo[0])
    #Atualiza o restante da matriz

    atualizar_restante_da_matriz(elemento_pivo[1], elemento_pivo[2])
    
    #Armazena a primeira linha da matriz como valores float
    linha_z = matriz[0].astype(float)
    #Filtra pelos valores menores que zero
    valores = linha_z[np.where(linha_z < 0)]

    #Variável de controle de fluxo
    x = input()

#Armazena o lucro da matriz
co.lucro_maximo = matriz[0,-1]
lucro = co.lucro_maximo

#Armazena o preço-sombra
co.preco_sombra = matriz[0, co.nConstantes:-1]
pSombra = co.preco_sombra

#Melhores pontos da matriz
co.melhor_pontos = matriz[1:, -1]
mPontos = co.melhor_pontos

co.variaveis_base = variaveis_base

#Saída de dados
print(f"Lucro ótimo = {lucro}")
print(f"Perços Sombra = {pSombra}")
print(f"Variáveis bases = {variaveis_base}" )
print(f"Melhores Pontos = {mPontos}")
print("Matriz final:")
print(matriz)