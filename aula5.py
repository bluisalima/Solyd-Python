''' Exercício - Aula 5: Faça um programa que leia a quantidade de pessoas que serão convidadas para uma festa.
Após isso o programa irá perguntar o nome de todas as pessoas e colocar numa lista de convidados.
Imprima todos os nomes da lista.
'''

numero_convidados = input("Número de pessoas convidadas: ")
convidados = []
i = 0
while i < int(numero_convidados):
    nome_convidado = input("Nome do convidado: ")
    convidados.append(nome_convidado)
    i += 1

print("Lista de convidados:\n")
for pessoas in convidados:
    print(pessoas)

