# Projeto: Promoção da Fórmula E

Este projeto foi desenvolvido com o intuito de promover a Fórmula E, utilizando algoritmos em Python para interação com usuários. A aplicação simula a organização e exibição de corridas, pilotos e suas respectivas pontuações, além de fornecer algumas funcionalidades interativas como comparação de desempenho entre pilotos e exportação de dados.

## Índice
1. [Descrição do Projeto](#descrição-do-projeto)
2. [Funcionalidades](#funcionalidades)
3. [Tecnologias Utilizadas](#tecnologias-utilizadas)
4. [Instalação e Execução](#instalação-e-execução)
5. [Como Usar](#como-usar)
6. [Exemplo de Uso](#exemplo-de-uso)
7. [Estrutura de Arquivos](#estrutura-de-arquivos)
8. [Contribuição](#contribuição)
9. [Licença](#licença)

## Descrição do Projeto

A Fórmula E é uma categoria de automobilismo focada em corridas de carros elétricos. Este projeto foi criado para fornecer uma ferramenta interativa que permite a visualização de corridas passadas, comparações entre pilotos e a exportação de dados sobre suas pontuações. Utilizamos o **pandas** para manipulação de dados e o projeto inclui várias funções que simulam um ambiente de interação voltado para o público fã de Fórmula E.

## Funcionalidades

- **Listagem de corridas**: Visualize as corridas da Fórmula E, com nomes e datas.
- **Comparação de pilotos**: Compare o desempenho de dois pilotos com base nos pontos obtidos.
- **Exibição de estatísticas de corridas**: Veja os resultados de uma corrida específica.
- **Filtragem de pilotos por pontuação**: Liste pilotos que tenham uma pontuação acima de um valor informado.
- **Exportação de dados**: Salve os dados dos pilotos em um arquivo CSV.

## Tecnologias Utilizadas

- **Linguagem**: Python 3.x
- **Bibliotecas**: 
  - [Pandas](https://pandas.pydata.org/) (para manipulação de dados)
  
## Instalação e Execução

### Pré-requisitos
- Python 3.x instalado na sua máquina.
- Instalar a biblioteca **pandas** via pip:
  ```bash
  pip install pandas

## Passos para execução

### Clone este repositório para a sua máquina local
    git clone https://github.com/seu-usuario/projeto-formula-e.git

### Acesse o diretório do projeto
    cd sprintpython

### Execute o script principal
    python main.py

### Como Usar

Ao executar o programa, em menu interativo será exibido com as seguintes opções

### 1. Listar Corridas: Mostra uma lista de corridas da Fórmula E.
### 2. Comparar Desempenho de Pilotos: Permite comparar o desempenho de dois pilotos com base na pontuação.
### 3. Exibir Estatísticas de uma Corrida: Exibe o resultado de uma corrida específica.
### 4. Listar Pilotos com Pontuação Acima de um Valor: Filtra os pilotos com base em uma pontuação mínima.
### 5. Salvar Dados de Pilotos em CSV: Salva os dados dos pilotos em um arquivo CSV.
### 6. Sair: Encerra o programa.

## Exemplo de Uso

### Exibindo Corridas

    Ao escolher a opção 1, o programa exibe todas as corridas disponíveis com suas respectivas datas:
    Escolha uma das opções:
    1. Listar Corridas
    2. Comparar Desempenho de Pilotos
    3. Exibir Estatísticas de uma Corrida
    4. Listar Pilotos com Pontuação Acima de um Valor
    5. Salvar Dados de Pilotos em CSV
    6. Sair
    Escolha uma opção: 1

    Corridas da Fórmula E:
    - ePrix de Roma (Data: 2024-04-13)
    - ePrix de Paris (Data: 2024-05-27)

### Comparando Pilotos
Na opção 2, você pode comparar o desempenho de dois pilotos:

Escolha uma opção: 2
Digite o nome do primeiro piloto: Nyck de Vries
Digite o nome do segundo piloto: Mitch Evans

Comparação entre Nyck de Vries e Mitch Evans:
Nyck de Vries | Pontos: 150
Mitch Evans | Pontos: 135

## Estrutura de Arquivos
projeto-formula-e/
│
├── main.py                 # Código principal com a lógica do programa
├── pilotos_formula_e.csv    # Arquivo gerado com dados de pilotos (após exportação)
├── README.md                # Documentação do projeto
└── requirements.txt         # Bibliotecas necessárias para execução
