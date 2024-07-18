#Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

try:
    var = str(input('Digite uma texto qualquer: '))

    var_2 = var.upper()

    print(f'O texto digitado em maiusculo é: {var_2}')
except KeyboardInterrupt:
    print('Vocë tem que inserir um texto')


