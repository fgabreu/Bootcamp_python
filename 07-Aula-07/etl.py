import csv

path_arquivo = "/Volumes/SSD Felipe/CURSOS ENGENHARIA DE DADOS/PYTHON CURSOS/PYTHON_BOOTCAMP/O7-Aula-07/vendas.csv"

#Funcao que le um arquivo csv e retorna uma lista de dicionarios
def ler_csv(nome_arquivo_csv: str) -> list[dict]:
    lista = []
    with open(nome_arquivo_csv, mode="r", encoding="utf-8") as arquivo:
        leitor = csv.DictReader(arquivo)
        for linha in leitor:
            lista.append(linha)
    return lista


#Funcao que faz o filtro de produtos qua ainda nao foram entregues
def filtrar_produtos_nao_entregues(lista: list[dict]) -> list[dict]:
    lista_produtos_filtrados = []
    for produto in lista:
        if produto.get("entregue") == "True":
            lista_produtos_filtrados.append(produto)
    return lista_produtos_filtrados

lista_de_produtos = ler_csv(path_arquivo)
produtos_entregues = filtrar_produtos_nao_entregues(lista_de_produtos)


#Funcao que soma os valores dos produtos
def somar_valores_dos_produtos(lista_produtos_filtrados: list[dict]) -> int:
    valor_total = 0
    for produto in lista_produtos_filtrados:
        valor_total += int(produto.get("preco"))
    return valor_total

