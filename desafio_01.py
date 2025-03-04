#Escreva um programa em Python que solicita ao usuário para digitar seu nome, 
# o valor do seu salário mensal e o valor do bônus que recebeu. 
# O programa deve, então, imprimir uma mensagem saudando o usuário pelo nome e informando 
# o valor do salário em comparação com o bônus recebido.

BONUS_CONT = 1000

#1. Solicite o nome do usuario
nome = input("Digite o seu nome: ")

#2. Digite o seu salario
salario = float(input("Digite o seu salário: "))

#3. Digite o valor do bonus recebido 
bonus = float(input("Digite o valor do seu bônus: "))

#4. Calcule o valor do bonus final 
valor_bonus = BONUS_CONT + salario * bonus 

#6. mensagem personalizada
print(f' Olá! {nome} muito bom te ter por aqui! \n você possui o bonus de {valor_bonus}')
