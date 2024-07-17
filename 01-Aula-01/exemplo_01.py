#Criar um programa onde o usuario digite dois valores e apareca a soma

valor_1 = float(input('Digite o primeiro valor: '))
valor_2 = float(input('Digite o segundo valor: '))

soma = sum(valor_1, valor_2)

print(f'A soma de {valor_1} com {valor_2} é {soma}')