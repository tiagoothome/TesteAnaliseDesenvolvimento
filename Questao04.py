#Questão 04: Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado:

#SP – R$67.836,43
#RJ – R$36.678,66
#MG – R$29.229,88
#ES – R$27.165,48
#Outros – R$19.849,53

#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora.

sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma = sp + rj + mg + es + outros

def perSP(sp):
    percentualSP = (sp*100) / soma
    return percentualSP

def perRJ(rj):
    percentualRJ = (rj*100) / soma
    return percentualRJ

def perMG(mg):
    percentualMG = (mg*100) / soma
    return percentualMG

def perES(es):
    percentualES = (es*100) / soma
    return percentualES

def perOutros(outros):
    percentualOutros = (outros*100) / soma
    return percentualOutros

n = perSP(sp)
print("A porcentagem do Estado de São Paulo é de %.2f" %(n))

n = perRJ(rj)
print("A porcentagem do Estado do Rio de Janeiro é de %.2f" %(n))

n = perMG(mg)
print("A porcentagem do Estado de Minas Gerais é de %.2f" %(n))

n = perES(es)
print("A porcentagem do Estado do Espírito Santo é de %.2f" %(n))

n = perOutros(outros)
print("A porcentagem dos outros estados é de %.2f" %(n))