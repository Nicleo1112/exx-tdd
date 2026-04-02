from main import filtrar_livros
from lista_livros import livros 

criterio_1 = {"Titulo": "Harry Potter", "Autor": "", "Ano": [], "livros": livros}
criterio_2 = {"Titulo": "", "Autor": "J.K Rowling", "Ano": [], "livros": livros}
criterio_3 = {"Titulo": "", "Autor": "", "Ano": [1997, 2020], "livros": livros}

resultado_1 = filtrar_livros(criterio_1)
print(resultado_1)

resultado_2 = filtrar_livros(criterio_2)
print(resultado_2)

resultado_3 = filtrar_livros(criterio_3)
print(resultado_3)
