# Questao 02: Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

#IMPORTANTE:
#Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

n = int(input("Insira um número: "))

t1 = 0
t2 = 1

print(t1)
print(t2)

cont = 3

while (1):
    t3 = t1 + t2
    print(t3)

    t1 = t2
    t2 = t3
    cont += 1

    if t3 < n:
        continue

    elif t3 == n:
        print("O número informado pertence a sequência de Fibonacci")
        break
    elif t3>n:
        print("O número informado não faz parte da sequência de Fibonacci")
        break





  