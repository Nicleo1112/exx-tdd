from lista_livros import filtro_livros

colecao_livros = [
    {"Titulo": "Harry Potter", "Autor": "J.K Rowling", "Ano": 1997},
    {"Titulo": "O Hobbit", "Autor": "Tolkien", "Ano": 1937},
    {"Titulo": "Python", "Autor": "Autor X", "Ano": 2020}
]

criterio_1 = {"Titulo": "Harry Potter", "Autor": "", "Ano": [], "livros": colecao_livros}
criterio_2 = {"Titulo": "", "Autor": "J.K Rowling", "Ano": [], "livros": colecao_livros}
criterio_3 = {"Titulo": "", "Autor": "", "Ano": [1997, 2020], "livros": colecao_livros}

resultado_1 = filtro_livros(criterio_1)
print(resultado_1)

resultado_2 = filtro_livros(criterio_2)
print(resultado_2)

resultado_3 = filtro_livros(criterio_3)
print(resultado_3)
