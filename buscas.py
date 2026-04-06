def busca_binaria(lista, nome_alvo):
    inf = 0
    sup = len(lista) - 1

    nome_alvo_lower = nome_alvo.lower()

    while inf <= sup:

        meio = (inf + sup) // 2
        nome_meio = lista[meio]["nome"].lower()

        if nome_meio == nome_alvo_lower:
            return lista[meio]

        elif nome_meio < nome_alvo_lower:
            inf = meio + 1

        else:
            sup = meio - 1

    return None


def busca_sequencial_filtro(lista, criterio, valor):
    resultados = []

    for jogador in lista:
        if jogador[criterio] == valor:
            resultados.append(jogador)

    return resultados
