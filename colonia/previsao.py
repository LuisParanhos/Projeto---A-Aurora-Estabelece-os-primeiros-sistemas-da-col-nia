import dados


def calcular_coeficientes(vento, energia):
    n = len(vento)

    # valida antes de calcular
    if n < 2:
        return 0, 0

    soma_x  = sum(vento)
    soma_y  = sum(energia)
    soma_xy = sum(vento[i] * energia[i] for i in range(n))
    soma_x2 = sum(vento[i] ** 2         for i in range(n))

    a = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x ** 2)
    b = (soma_y - a * soma_x) / n
    return a, b


def prever_energia(velocidade_vento):
    a, b = calcular_coeficientes(dados.historico_vento, dados.historico_energia)
    return round(a * velocidade_vento + b, 1)


def exibir_previsao():
    vento_atual = dados.obter_dados('vento')
    estimativa  = prever_energia(vento_atual)
    a, b        = calcular_coeficientes(dados.historico_vento, dados.historico_energia)
    print(f"  Vento atual: {vento_atual} m/s  |  Energia prevista: {estimativa} kW  (y = {a:.2f}x + {b:.2f})")
