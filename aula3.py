''' Exercício - Aula 3: Faça um programa que pergunte a idade, o peso e a altura de uma pessoa
e decide se ela está apta a entrar no Exército. Para isso é preciso ter mais de 18 anos,
pesar 60kg ou mais e medir 1.70 ou mais. '''

# Inicializando as variaveis
idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))
altura = float(input("Digite a altura: "))

# Testa os requisitos
if(idade > 17 and peso > 79 and altura > 1.69):
    print("Bem vindo ao Exercito!")
else:
    print("Você não tem os requisitos.")

# Autora: bluisalima