def filtrar_livros(criterio):
    resultado = []
    livros = criterio["livros"]

    for livro in livros:
        if criterio["Titulo"] != "" and criterio["Titulo"].lower() not in livro["Titulo"].lower():
            continue
        if criterio["Autor"] != "" and criterio["Autor"].lower() not in livro["Autor"].lower():
            continue
        if criterio["Ano"] != []:
            if livro["Ano"] < criterio["Ano"][0] or livro["Ano"] > criterio["Ano"][1]:
                continue
        resultado.append(livro)

    return resultado
