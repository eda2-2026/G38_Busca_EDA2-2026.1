# Organizador de Pelada

Conteúdo da Disciplina: Algoritmos de Busca

## Alunos
|Matrícula | Aluno |
| 231039178  |  Pedro Felipe Silva Vargas |

## Sobre
O projeto é um sistema de gerenciamento de jogadores para peladas semanais de futebol, informando a posição de cada jogador e se pagou o campo ou não. O projeto utilizou dois tipos de algoritmos para seu funcionamento:

- **Busca Binária**: utilizada para localizar um jogador pelo nome exato em uma lista ordenada alfabeticamente, com complexidade O(log n).
- **Busca Sequencial**: utilizada para filtrar jogadores por critérios como posição ou status de pagamento, percorrendo toda a lista com complexidade O(n).

O sistema permite adicionar, remover, buscar e filtrar jogadores, além de controlar quem já pagou o campo.

## Screenshots
Adicione 3 ou mais screenshots do projeto em funcionamento.

## Instalação
Linguagem: Python

Pré-requisitos:
- Python 3.6 ou superior instalado

```bash
git clone https://github.com/seu-usuario/G38_Busca_EDA2-2026.1.git
cd G38_Busca_EDA2-2026.1
```

## Uso

Execute o programa com:

```bash
python3 main.py
```

O menu interativo apresenta as seguintes opções:

1. **Adicionar Jogador** - Cadastra um novo jogador com nome, posição e status de pagamento
2. **Buscar Jogador** - Localiza um jogador pelo nome usando Busca Binária
3. **Listar Devedores** - Mostra quem ainda não pagou usando Busca Sequencial
4. **Filtrar por Posição** - Lista jogadores de uma posição específica usando Busca Sequencial
5. **Remover Jogador** - Remove um jogador da lista
6. **Alterar Status de Pagamento** - Alterna entre pago/não pago
7. **Listar Todos os Jogadores** - Exibe todos os cadastrados