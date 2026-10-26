# Mini sistemas no terminal

Pequenos programas em Python, com menu em laço, que simulam sistemas simples: estoque, caixa eletrônico, calculadora, votação e notas de aluno. Foram feitos durante os estudos de lógica de programação no curso de Ciência da Computação da UPF.

Todos funcionam pelo terminal: o programa mostra um menu, o usuário escolhe uma opção, e o menu volta até a opção de sair.

## Programas

| Arquivo | O que faz |
|---|---|
| `estoque.py` | Controle de estoque com limite de 10 unidades: adicionar, remover e consultar. Recusa quantidades negativas, zero ou que não cabem. |
| `caixa_eletronico.py` | Consulta de saldo, depósito e saque. O saldo é atualizado a cada operação e o saque é recusado se o saldo for insuficiente. |
| `calculadora.py` | Soma, subtração, multiplicação e divisão, com aviso na divisão por zero. |
| `votacao.py` | Contagem de votos entre três candidatos, com resultado final ao sair. |
| `sistema_notas.py` | Registra a nota de um aluno (0 a 10) e consulta a situação: aprovado, reprovado ou recuperação com nova nota. |

## Como executar

Precisa de Python 3 instalado. No terminal, dentro da pasta do repositório:

    python3 caixa_eletronico.py

## O que usei

- laço de repetição (`while True` com `break`) para manter o menu
- estruturas de decisão (`if`, `elif`, `else`)
- funções simples (`ler_inteiro` e `ler_decimal`) para repetir a pergunta quando o usuário digita algo que não é número
- formatação de texto com f-strings

## Possíveis melhorias

- salvar o saldo e o estoque em arquivo, para não zerar ao fechar o programa
- histórico de operações no caixa eletrônico
- vários alunos no sistema de notas

## Outros repositórios

- [batalha-por-turnos](https://github.com/ffogasso/batalha-por-turnos): jogo de batalha no terminal
- [exercicios-python](https://github.com/ffogasso/exercicios-python): exercícios de decisão, repetição e funções

## Sobre

Feito por Filipe Fogasso Torella, estudante de Ciência da Computação na UPF.
