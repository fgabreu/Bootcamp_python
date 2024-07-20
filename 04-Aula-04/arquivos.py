import csv

path_arquivo = str = "exemplo.csv"

arquivo_csv: list = []

with open(file=path_arquivo, mode = "r", encoding='utf-8') as arquivo:
    leitor_csv= csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)
