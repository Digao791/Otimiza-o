import re
import numpy as np
import controle as co

def retornar_matriz():

    #Através do REGEX, pego todos os coeficientes de Z
    coeficientes = re.findall(r'[-+]?\d*\.?\d+', co.funcao)
    coeficientes = [float(numero) for numero in coeficientes]
    coeficientes = [ -numero for numero in coeficientes] 
    co.nConstantes = len(coeficientes)


    #Linha Z criada
    linha_z = coeficientes + ([0.0] * len(co.restricoes) + [0])
    # *Colhendo os coeficientes das restrições
    restricoes = []
    
    index = 0
    for restricao in co.restricoes:
        #Através do REGEX, pego todos os coeficientes da restrição
        values = re.findall(r'[-+]?\d*\.?\d+', restricao[0])
        values = [float(numero) for numero in values]

        #Variáveis do simplex
        variaveis = [0.0]*len(co.restricoes)
        
        if restricao[1] == "<=":
            variaveis[index] = 1.0 
        elif restricao[1] == ">=":
            variaveis[index] = -1.0
        
        index+=1
        ld = [float(restricao[2])]
        restricoes.append(values + variaveis + ld)

    #Criando a matriz principal
    linhas = [linha_z] + [linha for linha in restricoes]

    matriz = np.zeros(shape=(len(co.restricoes) + 1,len(coeficientes) + len(co.restricoes)))
    matriz = np.vstack(linhas)
    matriz = matriz.astype(float)
  
    #Retornando a matriz principal
    return matriz
