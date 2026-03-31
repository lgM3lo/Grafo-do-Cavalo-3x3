# Trabalho Prático 2 — Grafo do Cavalo em Tabuleiro 3x3

## Membros
- Luis Guilherme Melo
- Jose Guilherme De Lima Ferreira Souza
- Natan Adams Nunes De Oliveira
- Samuel Moreira Vieira

## Descrição do projeto
Este projeto implementa, em **Python**, a modelagem do **grafo do cavalo** em um tabuleiro de xadrez **3x3**.

Cada casa do tabuleiro é representada por um **vértice** e cada movimento válido do cavalo entre duas casas é representado por uma **aresta**.

O programa lê o grafo a partir de um arquivo de entrada no **formato algs4**, constrói a estrutura usando **lista de adjacência** e responde às seguintes questões:

- exibe a lista de adjacência do grafo;
- identifica as **componentes conexas**;
- calcula a **distância mínima** entre `(0,0)` e `(2,2)`;
- verifica se o grafo possui **ciclo**;
- mostra os vértices de um ciclo encontrado.

---

## Objetivo do trabalho
O objetivo é aplicar conceitos de grafos usando uma situação prática: os movimentos do cavalo em um tabuleiro reduzido.

Além disso, o projeto utiliza algoritmos clássicos de grafos:

- **DFS (Depth-First Search)** para componentes conexas;
- **BFS (Breadth-First Search)** para menor caminho em grafo não ponderado;
- **DFS** para detecção de ciclo.

---

## Representação do tabuleiro
O tabuleiro 3x3 possui 9 casas, portanto o grafo possui 9 vértices.

A numeração usada foi:

```text
(0,0)=0   (0,1)=1   (0,2)=2
(1,0)=3   (1,1)=4   (1,2)=5
(2,0)=6   (2,1)=7   (2,2)=8
