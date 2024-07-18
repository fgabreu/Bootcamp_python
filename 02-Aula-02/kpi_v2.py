#DESAFIO: Calculo de bonus com entrada de usuario

constante_bonus = 1000

#1-Solicita ao usuaário que digite o seu nome
try: 
    nome = input("Digite o seu nome: ")

    if nome.isdigit():
        print("Voce digitou seu nome errado")
        exit()
    elif len(nome) == 0:
        print("Voce não digitou nada")
        exit()
    elif nome.isspace():
        print("Voce digiou so espaco")
        exit()
    else:
        print("Nome valido", nome)
except ValueError as e:
    print(e)

#2-Solicita ao usuário que digite o valor do seu salario
try:

    salario = float(input("Digite o seu salário: "))
    if salario < 0:
        print("Por favor, digite um valor positivo para o salário.")
except ValueError:
    print("Entrada inválida para o salário. Por favor, digite um número.")

#3-Solicita ao usuário que digite a porcentagem do bônus recebido
try:
    bonus = float(input("Digite o percentual do bônus recebido: "))
    if bonus < 0:
        print("Por favor, digite um valor positivo para o bônus.")
except ValueError:
    print("Entrada inválida para o bônus. Por favor, digite um número.")

#4-Calculo do KPI do bônus de 2024
kpi_bonus = constante_bonus + salario * bonus

#5-Imprimir a mensagem com o valor do bônus
print(f'Olá {nome}, o seu bônus foi de {kpi_bonus}')