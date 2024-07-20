''' 
Crie um dicionario para armazenar informacoes de um livro,
incluindo titulo, autor e ano de publicacao. Imprima cada informacao
'''

from typing import Dict, Any

livro_01: Dict[str, Any] = {
    "Titulo":"Pai Rico Pai Pobre",
    "Autor": "Robert Kyosaki",
    "Ano_publicacao": 1997
}

livro_02: Dict[str, Any] = {
    "Titulo":"O Segredos da Mente Milionaria",
    "Autor": "T. Harv Eker",
    "Ano_publicacao": 2005
}

lista_livros = []
lista_livros.append(livro_01)
lista_livros.append(livro_02)

print(lista_livros)

