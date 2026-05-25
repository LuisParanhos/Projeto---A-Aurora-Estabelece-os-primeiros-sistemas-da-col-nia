import dados


def calculo_energia_total():
    energia_total = 0
    for sistema in dados.sistemas['energetico'].values():
        if sistema['ativo']:
            energia_total += sistema['capacidade']
    return energia_total


def analisar_consumo(geracao=None, consumo=None):
    if geracao is None:
        geracao = calculo_energia_total()
    if consumo is None:
        consumo = dados.obter_dados('consumo')

    diferenca = geracao - consumo

    if diferenca < -20:
        return f"  CRITICO  | Falta de {abs(diferenca)} kW — reduzir consumo ou aumentar geração urgente."
    elif diferenca < 0:
        return f"  ALERTA   | Consumo maior que geração em {abs(diferenca)} kW."
    elif diferenca <= 10:
        return f"  OK       | Equilíbrio energético — diferença de apenas {abs(diferenca)} kW."
    else:
        return f"  SUGESTÃO | Excedente de {diferenca} kW — considere armazenar energia."


def exibir_analise():
    geracao = calculo_energia_total()
    consumo = dados.obter_dados('consumo')
    print(f"  Geração: {geracao} kW  |  Consumo: {consumo} kW")
    print(analisar_consumo(geracao, consumo))
