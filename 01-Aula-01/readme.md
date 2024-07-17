# Utilização do Programa de Cálculo de KPI

## Instruções:

1. O programa começa solicitando ao usuário que insira seu nome.
2. Em seguida, o programa pede ao usuário para inserir o valor do seu salário. Considere que este valor pode ser um número decimal.
3. Depois, o programa deve solicitar a porcentagem do bônus recebido pelo usuário, que também pode ser um número decimal.
4. O cálculo do KPI do bônus é feito através da seguinte fórmula:
    ```
    constante_bonus + salario * bonus
    ```
    **Nota:** Para o ano de 2024, o valor de `constante_bonus` é 1000.
5. Finalmente, o programa deve imprimir uma mensagem no seguinte formato: 
    ```
    "Olá [nome], o seu valor bônus foi de 5000"
    ```

## Exemplo de Uso:

Suponha que o usuário insira os seguintes valores:
- Nome: João
- Salário: 4000.50
- Bônus: 0.1 (10%)

O programa calculará o valor do bônus como segue:
1000 + 4000.50 * 0.1 = 1400.05

E exibirá a mensagem:
Olá João, o seu valor bônus foi de 1400.05
