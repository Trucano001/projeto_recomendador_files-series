import math

def coletar_avaliacoes(filmes, series):
    contador_filmes = 0 
    valores_x_inicial = []
    
    print("\n--- Avaliação de Filmes ---")
    for filme in filmes:
        while True:
            try:
                if contador_filmes >= 7:
                    avaliacao = int(input(f'Com qual nota de 0 a 5 você avalia a saga: {filme} (digite -1 caso ainda não tenha assistido): '))
                else:
                    avaliacao = int(input(f'Com qual nota de 0 a 5 você avalia o filme: {filme} (digite -1 caso ainda não tenha assistido): '))
                    
                if avaliacao == -1 or 0 <= avaliacao <= 5:
                    valores_x_inicial.append(avaliacao)
                    contador_filmes += 1
                    break
                else:
                    print('Valor inválido, digite de 0 a 5 ou -1.')
            except ValueError:
                print('Erro! Utilize apenas números inteiros válidos.')

    print("\n--- Avaliação de Séries ---")
    for serie in series:
        while True:
            try:
                avaliacao = int(input(f'Com qual nota de 0 a 5 você avalia a série: {serie} (digite -1 caso ainda não tenha assistido): '))
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
        
        numerador = sum(lista_sub_x[j] * lista_sub_y[j] for j in range(len(lista_sub_x)))
        denominador = math.sqrt(sum(sub**2 for sub in lista_sub_x) * sum(sub**2 for sub in lista_sub_y))
        
        r = 0 if denominador == 0 else numerador / denominador
        if r > 0:
            coeficientes.append((r, index_usuario))
        
    return coeficientes

def gerar_recomendacoes(usuarios_ordenados, valores_usuario, dados_y, filmes, series):
    filmes_recomendados = []
    series_recomendadas = []
    
    for _, index_usuario in usuarios_ordenados:
        usuario_alvo = dados_y[index_usuario]
        encontrou_algo = False
        
        for i in range(15):
            if usuario_alvo[i] != -1 and valores_usuario[i] == -1 and usuario_alvo[i] >= 4:
                if i >= 10:
                    nome_serie = series[i - 10]
                    if nome_serie not in series_recomendadas:
                        series_recomendadas.append(nome_serie)
                        encontrou_algo = True
                else:
                    nome_filme = filmes[i]
                    if nome_filme not in filmes_recomendados:
                        filmes_recomendados.append(nome_filme)
                        encontrou_algo = True
        
        if encontrou_algo:
            break
            
    return filmes_recomendados, series_recomendadas


filmes = ['Vingadores Ultimato', 'A Odisseia', 'A Ilha do medo', 'A Substância', 'Interestelar', 'Oppenheimer', 'Homem-Aranha', 'Crepúsculo', 'Harry Potter', 'Senhor dos Anéis']
series = ['Supernatural', 'Stranger Things', 'Game of Thrones', 'The boys', 'Wandinha']

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

valores_x_inicial = coletar_avaliacoes(filmes, series)

coeficientes_de_pearson = calcular_pearson(valores_x_inicial, dados_y)

if not coeficientes_de_pearson:
    print('\nNão há dados suficientes em comum para gerar uma recomendação.')
else:
    coeficientes_de_pearson.sort(key=lambda x: x[0], reverse=True)
    
    filmes_rec, series_rec = gerar_recomendacoes(coeficientes_de_pearson, valores_x_inicial, dados_y, filmes, series)
    
    print("\n==============================")
    if len(filmes_rec) == 0 and len(series_rec) == 0:
        print('Não temos nada para recomendar de acordo com esses dados.')
    else:
        if len(filmes_rec) > 0:
            print('🎬 Filmes recomendados:', ', '.join(filmes_rec))
        if len(series_rec) > 0:
            print('📺 Séries recomendadas:', ', '.join(series_rec))
    print("==============================") 