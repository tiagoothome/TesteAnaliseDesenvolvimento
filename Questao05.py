#Questão 05: Escreva um programa que inverta os caracteres de um string.

#IMPORTANTE:
#a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
#b) Evite usar funções prontas, como, por exemplo, reverse;


palavra = input("Digite uma palavra: ")

lista=[]
lista_inversa=[]

lista[:0] = palavra

for i in lista[::-1]:
    lista_inversa.append(i)

word = ''.join(map(str, lista_inversa))

print(word)