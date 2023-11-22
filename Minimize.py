import controle as co
import re
import numpy as np

def retornar_matriz():

    coeficientes = re.findall(r'[-+]?\d*\.?\d+', co.funcao)
    coeficientes = [float(numero) for numero in coeficientes]
    co.nConstantes = len(coeficientes)

    coeficientes.append(0)
    restricoes = []

    for restricao in co.restricoes:
        values = re.findall(r'[-+]?\d*\.?\d+', restricao[0])
        values = [float(numero) for numero in values]
        ld = [float(restricao[2])]
        restricoes.append(values + ld)

    matriz = [coeficientes] + [restricao for restricao in restricoes]
    matriz = np.vstack(matriz)

    new_matriz = matriz.copy()

    for i in range(len(coeficientes) - 1):
        new_matriz[0,i] = matriz[-(i + 1),-1]
        new_matriz[i + 1,-1] = matriz[0, -2 -i]
    
    novos_coeficientes = [new_coeficiente for new_coeficiente in new_matriz[0, :-1]]
    novos_coeficientes = [float(value) for value in novos_coeficientes]
    novos_coeficientes = [-value for value in novos_coeficientes]

    linha_z = novos_coeficientes + ([0.0]* len(co.restricoes) + [0])
    
    restricoes = []
    index = 0
    for restricao in new_matriz[1:,:]:
        valor = [float(value) for value in restricao[:-1]]
        variaveis = [0.0]*(len(co.restricoes))
        if co.restricoes[index][1] == "<=":
            variaveis[index] = -1.0
        elif co.restricoes[index][1] == ">=":
            variaveis[index] = 1.0
        index+=1
        ld = [restricao[2]]
        restricoes.append(valor + variaveis + ld)
    
    linhas = [linha_z] + [linha for linha in restricoes]
    matriz = np.zeros(shape=(len(co.restricoes) + 1,len(coeficientes) + len(co.restricoes)))
    matriz = np.vstack(linhas)
    matriz = matriz.astype(float)
    
    return matriz
    

