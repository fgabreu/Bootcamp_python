#DESAFIO: Calculo de bonus com entrada de usuario

constante_bonus = 1000

#1-Solicita ao usuaário que digite o seu nome
nome = input("Digite o seu nome: ")

#2-Solicita ao usuário que digite o valor do seu salario
salario = float(input("Digite o seu salário: "))

#3-Solicita ao usuário que digite a porcentagem do bônus recebido
bonus = float(input("Digite o percentual do bônus recebido: "))

#4-Calculo do KPI do bônus de 2024
kpi_bonus = constante_bonus + salario * bonus

#5-Imprimir a mensagem com o valor do bônus
print(f'Olá {nome}, o seu bônus foi de {kpi_bonus}')