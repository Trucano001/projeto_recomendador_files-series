# Sistema de Recomendação de Filmes e Séries

## Sobre o projeto

Este projeto foi desenvolvido como parte de um trabalho acadêmico da disciplina de Introdução à Computação, com o tema **Algoritmos e Sociedade**.

O objetivo é desenvolver um sistema simples de recomendação de filmes e séries utilizando avaliações de usuários e o cálculo de similaridade entre eles.

O programa analisa as notas atribuídas pelos usuários a diferentes filmes e séries para identificar pessoas com gostos semelhantes e, a partir disso, sugerir conteúdos que o usuário ainda não assistiu.

## Arquivos do projeto

O repositório contém duas versões do sistema:

### 1. Sistema sem pesos (`projeto_sem_pesos.py`)

Esta é a versão inicial do algoritmo.

- Calcula a similaridade entre os usuários utilizando o coeficiente de correlação de Pearson.
- Identifica usuários com avaliações semelhantes.
- Utiliza as avaliações desses usuários para gerar recomendações.
- Não aplica um fator de peso para diferenciar a influência de cada usuário.

### 2. Sistema com pesos (`projeto_com_pesos.py`)

Esta é a versão aprimorada do algoritmo.

- Mantém o cálculo de similaridade utilizando Pearson.
- Aplica um fator de peso à similaridade de cada usuário.
- Usuários com maior similaridade exercem maior influência nas recomendações.
- Calcula a média ponderada das avaliações dos conteúdos.
- Recomenda conteúdos cuja média ponderada seja igual ou superior a 4.

O fator de peso permite observar como a influência dos usuários muda de acordo com o grau de similaridade.

## Como funciona o algoritmo?

O sistema utiliza uma matriz de avaliações, na qual cada linha representa um usuário e cada coluna representa um filme ou uma série.

As avaliações seguem estas regras:

- **0 a 5:** nota atribuída ao conteúdo.
- **-1:** indica que o usuário não assistiu ou não avaliou aquele conteúdo.

O coeficiente de Pearson é utilizado para medir a semelhança entre as avaliações de dois usuários. Quanto mais próxima a correlação positiva estiver de 1, maior será a similaridade entre eles.

Na versão com pesos, essa similaridade também é utilizada para determinar a influência de cada usuário na recomendação.

## Tecnologias utilizadas

- Python
- Biblioteca `math`
- Coeficiente de correlação de Pearson
- Sistema de recomendação baseado em similaridade entre usuários

## Como executar

1. Instale o Python em seu computador.
2. Baixe ou clone este repositório.
3. Abra a pasta do projeto em um editor de código ou terminal.
4. Execute o arquivo da versão desejada.

Exemplo:

```bash
python projeto_sem_pesos.py
```

Ou, para executar a versão com pesos:

```bash
python projeto_com_pesos.py
```

Durante a execução, o programa solicitará as avaliações dos filmes e das séries e, posteriormente, apresentará as recomendações.

## Objetivo acadêmico

Além de desenvolver um algoritmo de recomendação, o projeto busca demonstrar como os dados utilizados e os critérios de cálculo podem influenciar os resultados apresentados por sistemas automatizados.

Também permite observar como a aplicação de pesos pode alterar a influência dos usuários e, consequentemente, as recomendações geradas.

---

**Projeto desenvolvido para a disciplina de Introdução à Computação — Tema: Algoritmos e Sociedade.**