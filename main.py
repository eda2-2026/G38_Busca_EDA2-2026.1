from dados import carregar_dados, salvar_dados
from buscas import busca_binaria, busca_sequencial_filtro

POSICOES_VALIDAS = ["Goleiro", "Zagueiro", "Meio", "Atacante"]

SEPARADOR = "═" * 50
SEPARADOR_FINO = "─" * 50


def exibir_cabecalho():
    print(f"\n{SEPARADOR}")
    print("   ORGANIZADOR DE PELADA")
    print(f"{SEPARADOR}")


def exibir_menu():
    print(f"\n{SEPARADOR_FINO}")
    print("  [1] Adicionar Jogador")
    print("  [2] Buscar Jogador (por Nome) — Busca Binaria")
    print("  [3] Listar Devedores — Busca Sequencial")
    print("  [4] Filtrar por Posicao — Busca Sequencial")
    print("  [5] Remover Jogador")
    print("  [6] Alterar Status de Pagamento")
    print("  [7] Listar Todos os Jogadores")
    print("  [0] Sair")
    print(SEPARADOR_FINO)


def exibir_jogador(jogador):
    status = "Pago" if jogador["pago"] else "Nao pagou"
    print(f"  Nome: {jogador['nome']}")
    print(f"  Posicao: {jogador['posicao']}")
    print(f"  Pagamento: {status}")


def exibir_lista_jogadores(jogadores, titulo="Jogadores"):
    if not jogadores:
        print("\n  [!] Nenhum jogador encontrado.")
        return

    print(f"\n  {titulo} ({len(jogadores)} encontrado(s)):")
    print(f"  {'No':<4} {'Nome':<20} {'Posicao':<12} {'Pagamento':<12}")
    print(f"  {'--':<4} {'----':<20} {'-------':<12} {'---------':<12}")

    for i, j in enumerate(jogadores, 1):
        status = "Pago" if j["pago"] else "Deve"
        print(f"  {i:<4} {j['nome']:<20} {j['posicao']:<12} {status:<12}")


def ler_opcao(mensagem, opcoes_validas):
    while True:
        escolha = input(mensagem).strip()
        if escolha in opcoes_validas:
            return escolha
        print(f"  [!] Opcao invalida. Escolha entre: {', '.join(opcoes_validas)}")


def adicionar_jogador(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  ADICIONAR JOGADOR")
    print(SEPARADOR_FINO)

    nome = input("  Nome do jogador: ").strip()
    if not nome:
        print("  [!] Nome nao pode ser vazio.")
        return

    if busca_binaria(lista, nome):
        print(f"  [!] O jogador '{nome}' ja esta cadastrado!")
        return

    print("  Posicoes disponiveis:")
    for i, pos in enumerate(POSICOES_VALIDAS, 1):
        print(f"    [{i}] {pos}")

    escolha_pos = ler_opcao("  Escolha a posicao (1-4): ",
                            [str(i) for i in range(1, 5)])
    posicao = POSICOES_VALIDAS[int(escolha_pos) - 1]

    escolha_pago = ler_opcao("  Ja pagou? (s/n): ", ["s", "n", "S", "N"])
    pago = escolha_pago.lower() == "s"

    novo_jogador = {
        "nome": nome,
        "posicao": posicao,
        "pago": pago
    }

    lista.append(novo_jogador)
    salvar_dados(lista)

    print(f"\n  Jogador '{nome}' adicionado com sucesso!")


def buscar_jogador(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  BUSCAR JOGADOR (Busca Binaria)")
    print(SEPARADOR_FINO)

    nome = input("  Nome do jogador: ").strip()
    if not nome:
        print("  [!] Nome nao pode ser vazio.")
        return

    print(f"\n  Executando Busca Binaria por '{nome}'...")

    jogador = busca_binaria(lista, nome)

    if jogador:
        print(f"\n  Jogador encontrado!")
        print(SEPARADOR_FINO)
        exibir_jogador(jogador)
        print(SEPARADOR_FINO)
    else:
        print(f"  Jogador '{nome}' nao encontrado na lista.")


def listar_devedores(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  DEVEDORES (Busca Sequencial)")
    print(SEPARADOR_FINO)

    print("  Executando Busca Sequencial por 'pago == False'...")

    devedores = busca_sequencial_filtro(lista, "pago", False)
    exibir_lista_jogadores(devedores, titulo="Jogadores Devedores")

    if devedores:
        total = len(devedores)
        print(f"\n  [!] {total} jogador(es) ainda nao pagaram o campo!")


def filtrar_por_posicao(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  FILTRAR POR POSICAO (Busca Sequencial)")
    print(SEPARADOR_FINO)

    print("  Posicoes disponiveis:")
    for i, pos in enumerate(POSICOES_VALIDAS, 1):
        print(f"    [{i}] {pos}")

    escolha = ler_opcao("  Escolha a posicao (1-4): ",
                        [str(i) for i in range(1, 5)])
    posicao = POSICOES_VALIDAS[int(escolha) - 1]

    print(f"\n  Executando Busca Sequencial por 'posicao == {posicao}'...")

    filtrados = busca_sequencial_filtro(lista, "posicao", posicao)
    exibir_lista_jogadores(filtrados, titulo=f"Jogadores - {posicao}")


def remover_jogador(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  REMOVER JOGADOR")
    print(SEPARADOR_FINO)

    nome = input("  Nome do jogador a remover: ").strip()
    if not nome:
        print("  [!] Nome nao pode ser vazio.")
        return

    jogador = busca_binaria(lista, nome)

    if not jogador:
        print(f"  Jogador '{nome}' nao encontrado.")
        return

    print("\n  Jogador encontrado:")
    exibir_jogador(jogador)

    confirmacao = ler_opcao("\n  Confirma remocao? (s/n): ", ["s", "n", "S", "N"])
    if confirmacao.lower() == "s":
        lista.remove(jogador)
        salvar_dados(lista)
        print(f"  Jogador '{nome}' removido com sucesso!")
    else:
        print("  Remocao cancelada.")


def alterar_pagamento(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  ALTERAR STATUS DE PAGAMENTO")
    print(SEPARADOR_FINO)

    nome = input("  Nome do jogador: ").strip()
    if not nome:
        print("  [!] Nome nao pode ser vazio.")
        return

    jogador = busca_binaria(lista, nome)

    if not jogador:
        print(f"  Jogador '{nome}' nao encontrado.")
        return

    status_atual = "Pago" if jogador["pago"] else "Nao pagou"
    print(f"\n  Status atual de '{nome}': {status_atual}")

    jogador["pago"] = not jogador["pago"]
    salvar_dados(lista)

    novo_status = "Pago" if jogador["pago"] else "Nao pagou"
    print(f"  Novo status de '{nome}': {novo_status}")


def listar_todos(lista):
    print(f"\n{SEPARADOR_FINO}")
    print("  TODOS OS JOGADORES")
    print(SEPARADOR_FINO)

    exibir_lista_jogadores(lista, titulo="Lista Completa")


def main():
    exibir_cabecalho()

    lista = carregar_dados()
    print(f"  {len(lista)} jogador(es) carregado(s) do arquivo.")

    while True:
        exibir_menu()
        opcao = input("  Escolha uma opcao: ").strip()

        if opcao == "1":
            adicionar_jogador(lista)

        elif opcao == "2":
            buscar_jogador(lista)

        elif opcao == "3":
            listar_devedores(lista)

        elif opcao == "4":
            filtrar_por_posicao(lista)

        elif opcao == "5":
            remover_jogador(lista)

        elif opcao == "6":
            alterar_pagamento(lista)

        elif opcao == "7":
            listar_todos(lista)

        elif opcao == "0":
            print(f"\n{SEPARADOR}")
            print("  Ate a proxima pelada! Valeu!")
            print(SEPARADOR)
            break

        else:
            print("  [!] Opcao invalida. Tente novamente.")


if __name__ == "__main__":
    main()
