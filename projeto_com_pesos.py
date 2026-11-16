import math

filmes = ['Vingadores Ultimato','A Odisseia','A Ilha do medo','A Substância','Interestelar','Oppenheimer','Homem-Aranha','Crepúsculo','Harry Potter','Senhor dos Anéis']

series = ['Supernatural','Stranger Things','Game of Thrones','The boys','Wandinha']

dados_y = [[5, 4, 3, 3, 5, 3, -1, -1, 5, 5, 4, 3, 4, -1, -1],
          [5, 4, 4, 4, 5, 5, 5, -1, -1, -1, 3, -1, 5, 3, -1],
          [5, -1, -1, -1, 5, -1, 4, 0, 5, -1, 3, 4, 5, -1, -1],
          [5, 5, 4, 4, 5, 5, 5, 2, 5, 5, 5, 4, 5, 5, 4],
          [5, -1, -1, -1, 5, -1, 5, 3, 5, 2, 5, 4, 5, 4, 3],
          [5, -1, -1, -1, -1, -1, 5, -1, 3, -1, -1, 3, -1, -1, -1],
          [-1, 2, 3, 5, 4, 5, 3, 2, -1, 5, 5, 4, 2, 5, 1],
          [5, 5, 4, -1, 5, 4, 5, -1, -1, -1, 5, 5, -1, -1, -1],
          [5, 3, 4, -1, 5, 4, 5, -1, -1, 5, 5, -1, 5, -1, -1],
          [5, -1, 5, 3, 4, 3, 5, -1, 5, 5, -1, 3, -1, 2, 0],
          [3, -1, 4, 4, 3, 4, 5, 0, 4, 2, 4, 3, -1, 2, 1],
          [5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5],
          [0, 3, -1, 5, 0, 5, 5, 5, 4, -1, 0, 1, 2, 3, 5],
          [4, 5, 4, 3, 5, 4, 3, 4, -1, 5, 4, 3, 5, 4, 3],
          [3, 4, 5, 5, 4, 5, 4, 3, 5, 4, -1, 5, 4, 3, 5],
          [5, 3, 4, 4, 5, 3, 5, 4, 3, 5, 4, -1, 5, 3, 4],
          [2, 3, 2, 4, 3, 4, 2, 5, 4, 3, 2, 4, 3, 5, -1],
          [4, 2, 3, 5, 4, 2, 5, 3, 4, 2, 5, 4, 3, 5, 4],
          [0, 0, 0, -1, 0, -1, 0, 0, 0, -1, 0, -1, -1, 0, 5],
          [4, 5, 3, -1, 5, 4, 3, 1, 5, 3, -1, 5, 3, 3, 3],
          [5, 4, 4, -1, 5, 2, -1, 3, 5, 4, 4, 3, -1, 3, 1]]

def coletar_avaliacoes(filmes, series):
    contador_filmes = 0
    valores_x_inicial = []

    print("\n--- Avaliação de Filmes ---")

    for filme in filmes:
        while True:
            try:
                if contador_filmes >= 7:
                    avaliacao = int(input(
                        f'Com qual nota de 0 a 5 você avalia a saga: {filme} '
                        '(digite -1 caso ainda não tenha assistido): '))
                else:
                    avaliacao = int(input(
                        f'Com qual nota de 0 a 5 você avalia o filme: {filme} '
                        '(digite -1 caso ainda não tenha assistido): '
                    ))

                if avaliacao == -1 or 0 <= avaliacao <= 5:
                    valores_x_inicial.append(avaliacao)
                    contador_filmes += 1
                    break

                else:
                    print('Valor inválido, digite um valor de 0 a 5 ou -1.')

            except ValueError:
                print('Erro! Utilize apenas números inteiros válidos.')

    print("\n--- Avaliação de Séries ---")

    for serie in series:
        while True:
            try:
                avaliacao = int(input(f'Com qual nota de 0 a 5 você avalia a série: {serie} ''(digite -1 caso ainda não tenha assistido): '))

                if avaliacao == -1 or 0 <= avaliacao <= 5:
                    valores_x_inicial.append(avaliacao)
                    break

                else:
                    print('Valor inválido, digite de 0 a 5 ou -1.')

            except ValueError:
                print('Erro! Utilize apenas números inteiros válidos.')

    return valores_x_inicial

def calcular_pearson(valores_usuario, dados_y):
    coeficientes = []

    for index_usuario, dado in enumerate(dados_y):
        valores_x_f = []
        valores_y_f = []

        for i in range(len(valores_usuario)):
            if valores_usuario[i] != -1 and dado[i] != -1:
                valores_x_f.append(valores_usuario[i])
                valores_y_f.append(dado[i])

        if len(valores_x_f) < 3:
            continue

        media_x = sum(valores_x_f) / len(valores_x_f)
        media_y = sum(valores_y_f) / len(valores_y_f)

        lista_sub_x = [xi - media_x for xi in valores_x_f]
        lista_sub_y = [yi - media_y for yi in valores_y_f]

        numerador = sum(lista_sub_x[j] * lista_sub_y[j]for j in range(len(lista_sub_x)))

        denominador = math.sqrt(
            sum(sub**2 for sub in lista_sub_x) *
            sum(sub**2 for sub in lista_sub_y))
        r = 0 if denominador == 0 else numerador / denominador

        if r > 0:
            coeficientes.append((r, index_usuario))

    return coeficientes

def gerar_recomendacoes_ponderadas(usuarios_ordenados,valores_usuario,dados_y,filmes,series,fator_peso):
    soma_filmes = {}
    soma_series = {}
    pesos_filmes = {}
    pesos_series = {}
    for r, index_usuario in usuarios_ordenados:
        usuario_alvo = dados_y[index_usuario]
        peso_vizinho = r ** fator_peso
        for i in range(len(filmes) + len(series)):
            if usuario_alvo[i] != -1 and valores_usuario[i] == -1:
                nota_dada = usuario_alvo[i]
                pontuacao_item = nota_dada * peso_vizinho
                if i >= len(filmes):
                    nome = series[i - len(filmes)]
                    soma_series[nome] = (soma_series.get(nome, 0) + pontuacao_item)
                    pesos_series[nome] = (pesos_series.get(nome, 0) + peso_vizinho)
                else:
                    nome = filmes[i]
                    soma_filmes[nome] = (soma_filmes.get(nome, 0) + pontuacao_item)
                    pesos_filmes[nome] = (pesos_filmes.get(nome, 0) + peso_vizinho)

    filmes_ordenados = [(nome, soma_filmes[nome] / pesos_filmes[nome]) for nome in soma_filmes if pesos_filmes[nome] > 0 and soma_filmes[nome] / pesos_filmes[nome] >= 4]
    series_ordenadas = [(nome, soma_series[nome] / pesos_series[nome]) for nome in soma_series if pesos_series[nome] > 0 and soma_series[nome] / pesos_series[nome] >= 4]

    filmes_ordenados.sort(key=lambda x: x[1], reverse=True)
    series_ordenadas.sort(key=lambda x: x[1], reverse=True)
    filmes_recomendados = [item[0] for item in filmes_ordenados]
    series_recomendadas = [item[0] for item in series_ordenadas]

    return filmes_recomendados, series_recomendadas

valores_usuario = coletar_avaliacoes(filmes, series)

usuarios_ordenados = calcular_pearson(valores_usuario, dados_y)

usuarios_ordenados.sort(key=lambda x: x[0], reverse=True)

if not usuarios_ordenados:
    print("\nNão foram encontrados usuários suficientemente semelhantes.")

else:
    while True:
        try:
            print('OBS: 1.0 = Peso padrão | Peso > 1.0 = Exige mais similaridade | 0.0 < Peso < 1.0 = Mais flexível')
            fator_peso = float(input("\nDigite o fator de peso (maior que zero): "))
            if fator_peso > 0:
                break
            else:
                print("O fator de peso deve ser maior que zero.")

        except ValueError:
            print("Digite um número válido.")

    filmes_recomendados, series_recomendadas = (gerar_recomendacoes_ponderadas(usuarios_ordenados,valores_usuario,dados_y,filmes,series,fator_peso))

    print("\n========== RECOMENDAÇÕES ==========")

    print("\n🎬 Filmes recomendados:")
    if filmes_recomendados:
        for filme in filmes_recomendados:
            print("-", filme)
    else:
        print("Não temos nenhum filme para recomendar")

    print("\n🎬 Séries recomendadas:")
    if series_recomendadas:
        for serie in series_recomendadas:
            print("-", serie)
    else:
        print("Não temos nenhuma série para recomendar")