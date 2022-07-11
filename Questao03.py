#Questão 03: Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
#• O menor valor de faturamento ocorrido em um dia do mês;
#• O maior valor de faturamento ocorrido em um dia do mês;
#• Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

#IMPORTANTE:
#a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
#b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

import json

def open_json():
    with open('dados.json') as f:
        entrada = json.load(f)

    return entrada


def menorValor(entrada):
    menorValor = entrada[0]["valor"]

    for valor in entrada:
        if valor["valor"] < menorValor:
            menorValor = valor["valor"]

    return menorValor


def maiorValor(entrada):
    maiorValor = entrada[0]["valor"]

    for valor in entrada:
        if valor["valor"] > maiorValor:
            maiorValor = valor["valor"]
        
    return maiorValor


def valorSuperior(entrada):
    somatorio = 0
    nDias = 0
    nDiasSup = 0

    for valor in entrada:
        faturamento = valor["valor"]
        if faturamento == 0:
            continue
        else:
            somatorio = somatorio + faturamento
            nDias = nDias + 1

    media = somatorio / nDias
   
    for valor in entrada:

        faturamento = valor["valor"]
        if faturamento > media:
            nDiasSup = nDiasSup + 1
    
    return nDiasSup


entrada = open_json()

n = menorValor(entrada)
print("O menor valor de faturamento ocorrido em um dia do mês foi: ", n)

n = maiorValor(entrada)
print("O maior valor de faturamento ocorrido em um dia do mês foi: ", n)

n = valorSuperior(entrada)
print("Número de dias no mês em que o valor de faturamento diário foi superior à média mensal foi: ", n)


