import json
import os

ARQUIVO_DADOS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "jogadores.json")


def carregar_dados():
    if not os.path.exists(ARQUIVO_DADOS):
        return []

    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as arquivo:
        dados = json.load(arquivo)
    return dados


def salvar_dados(lista):
    lista.sort(key=lambda jogador: jogador["nome"].lower())

    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as arquivo:
        json.dump(lista, arquivo, indent=4, ensure_ascii=False)
