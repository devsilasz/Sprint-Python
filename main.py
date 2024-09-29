import pandas as pd  # Importa a biblioteca pandas para manipulação de dados.

def main():
    # Lista de dicionários representando as corridas e seus resultados.
    corridas = [
        {"nome": "ePrix de Roma", "data": "2024-04-13",
         "resultados": [{"nome": "Nyck de Vries", "pontos": 25}, {"nome": "Jean-Éric Vergne", "pontos": 18}]},
        {"nome": "ePrix de Paris", "data": "2024-05-27",
         "resultados": [{"nome": "Mitch Evans", "pontos": 25}, {"nome": "Lucas di Grassi", "pontos": 18}]}
    ]

    # Lista de dicionários representando pilotos e seus dados.
    pilotos = [
        {"nome": "Nyck de Vries", "equipe": "Mercedes-EQ", "pontos": 150},
        {"nome": "Jean-Éric Vergne", "equipe": "DS Techeetah", "pontos": 140},
        {"nome": "Mitch Evans", "equipe": "Jaguar Racing", "pontos": 135},
        {"nome": "Lucas di Grassi", "equipe": "Audi Sport ABT", "pontos": 120}
    ]

    # Converte a lista de pilotos em um DataFrame do pandas para facilitar a manipulação dos dados.
    df_pilotos = pd.DataFrame(pilotos)

    while True:
        menu()  # Exibe o menu de opções.
        opcao = input("Escolha uma opção: ")  # Recebe a opção escolhida pelo usuário.

        # Verifica qual opção o usuário escolheu e chama a função correspondente.
        if opcao == "1":
            listar_corridas(corridas)  # Lista todas as corridas.
        elif opcao == "2":
            # Recebe os nomes de dois pilotos e compara seus desempenhos.
            piloto1 = input("Digite o nome do primeiro piloto: ")
            piloto2 = input("Digite o nome do segundo piloto: ")
            comparar_desempenho_pilotos(df_pilotos, piloto1, piloto2)
        elif opcao == "3":
            # Recebe o nome de uma corrida e exibe suas estatísticas.
            nome_corrida = input("Digite o nome da corrida: ")
            exibir_estatisticas_corrida(corridas, nome_corrida)
        elif opcao == "4":
            # Lista os pilotos com pontuação acima de um valor específico.
            listar_pilotos_acima_de(df_pilotos)
        elif opcao == "5":
            # Salva os dados dos pilotos em um arquivo CSV.
            salvar_dados_em_csv(df_pilotos)
        elif opcao == "6":
            print("Saindo...")  # Encerra o programa.
            break
        else:
            # Caso o usuário insira uma opção inválida, exibe uma mensagem de erro.
            print("Opção inválida. Tente novamente.")

# Função que exibe o menu de opções para o usuário.
def menu():
    print("\nEscolha uma das opções:")
    print("1. Listar Corridas")
    print("2. Comparar Desempenho de Pilotos")
    print("3. Exibir Estatísticas de uma Corrida")
    print("4. Listar Pilotos com Pontuação Acima de um Valor")
    print("5. Salvar Dados de Pilotos em CSV")
    print("6. Sair")

# Função para listar todas as corridas disponíveis.
def listar_corridas(corridas):
    print("\nCorridas da Fórmula E:")
    # Percorre a lista de corridas e imprime o nome e a data de cada uma.
    for corrida in corridas:
        print(f" - {corrida['nome']} (Data: {corrida['data']})")

# Função que encontra um piloto no DataFrame com base no nome.
def encontrar_piloto(df, nome):
    # Usa o pandas para encontrar o piloto cujo nome corresponde ao fornecido (ignora maiúsculas/minúsculas).
    piloto = df[df['nome'].str.lower() == nome.lower()]
    if not piloto.empty:
        return piloto.iloc[0]  # Retorna o primeiro resultado encontrado.
    return None  # Retorna None se o piloto não for encontrado.

# Função que compara o desempenho de dois pilotos.
def comparar_desempenho_pilotos(df, nome_piloto1, nome_piloto2):
    # Encontra os dois pilotos com base em seus nomes.
    piloto1 = encontrar_piloto(df, nome_piloto1)
    piloto2 = encontrar_piloto(df, nome_piloto2)

    # Verifica se os pilotos foram encontrados. Caso contrário, exibe mensagem de erro.
    if piloto1 is None:
        print(f"\nPiloto {nome_piloto1} não encontrado")
        return
    if piloto2 is None:
        print(f"\nPiloto {nome_piloto2} não encontrado")
        return

    # Exibe a comparação entre os dois pilotos.
    print(f"\nComparação entre {piloto1['nome']} e {piloto2['nome']}:")
    print(f"{piloto1['nome']} | Pontos: {piloto1['pontos']}")
    print(f"{piloto2['nome']} | Pontos: {piloto2['pontos']}")

# Função para encontrar uma corrida com base no nome.
def encontrar_corrida(corridas, nome_corrida):
    # Percorre a lista de corridas e retorna a corrida correspondente ao nome informado.
    for corrida in corridas:
        if corrida['nome'].lower() == nome_corrida.lower():
            return corrida
    return None  # Retorna None se a corrida não for encontrada.

# Função que exibe as estatísticas de uma corrida específica.
def exibir_estatisticas_corrida(corridas, nome_corrida):
    corrida = encontrar_corrida(corridas, nome_corrida)  # Busca a corrida pelo nome.

    if corrida:
        # Exibe os detalhes da corrida encontrada.
        print(f"\nEstatísticas da corrida {corrida['nome']}:")
        print(f"Data: {corrida['data']}")
        print("Pilotos e Pontos:")
        # Exibe os resultados (nome do piloto e seus pontos) para essa corrida.
        for piloto in corrida['resultados']:
            print(f"- {piloto['nome']}: {piloto['pontos']} pontos")
    else:
        print("\nCorrida não encontrada.")  # Mensagem caso a corrida não seja encontrada.

# Função para listar pilotos com pontuação acima de um valor informado pelo usuário.
def listar_pilotos_acima_de(df):
    try:
        # Solicita ao usuário um valor mínimo de pontuação e converte para inteiro.
        pontuacao_minima = int(input("Digite a pontuação mínima: "))
    except ValueError:
        # Caso o valor inserido não seja um número, exibe mensagem de erro.
        print("Por favor, insira um número válido.")
        return

    # Filtra o DataFrame para mostrar apenas pilotos com pontuação acima ou igual ao valor informado.
    filtrado = df[df['pontos'] >= pontuacao_minima]
    if filtrado.empty:
        print(f"Nenhum piloto com mais de {pontuacao_minima} pontos.")  # Mensagem se nenhum piloto corresponder ao critério.
    else:
        # Exibe os pilotos que têm pontuação acima do valor informado.
        print(f"\nPilotos com mais de {pontuacao_minima} pontos:")
        print(filtrado[['nome', 'equipe', 'pontos']])

# Função para salvar os dados dos pilotos em um arquivo CSV.
def salvar_dados_em_csv(df):
    nome_arquivo = "pilotos_formula_e.csv"  # Nome do arquivo onde os dados serão salvos.
    df.to_csv(nome_arquivo, index=False)  # Usa o método pandas para salvar o DataFrame em formato CSV.
    print(f"Dados salvos com sucesso em {nome_arquivo}")  # Mensagem de confirmação ao salvar o arquivo.

# Execução principal do programa.
main()  # Chama a função principal que controla o fluxo do programa.
