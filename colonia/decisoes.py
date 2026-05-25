import dados


def avaliar_regras():
    energia = dados.obter_dados('energia')
    consumo = dados.obter_dados('consumo')
    clima   = dados.obter_dados('clima')
    acoes   = []

    # Regra 1: energia crítica
    if energia < 20:
        acoes.append('CRITICO  | Energia abaixo de 20% — sistemas não essenciais desligados.')
        desligar_nao_essenciais()

    # Regra 2: energia baixa E consumo alto
    elif energia < 50 and consumo > 60:
        acoes.append('ALERTA   | Energia baixa com consumo alto — modo economia ativado.')
        desligar_nao_essenciais()

    # Regra 3: energia baixa
    elif energia < 50:
        acoes.append('AVISO    | Energia abaixo de 50% — reduzir consumo não essencial.')

    # Regra 4: tudo normal
    else:
        acoes.append('OK       | Energia em nível seguro — operação normal.')

    # Regra 5: clima desfavorável
    if clima in ('nublado', 'tempestade'):
        acoes.append(f"INFO     | Clima '{clima}' — priorizar geração eólica.")

    # Regra 6: suporte à vida sempre garantido
    garantir_suporte_vida()
    acoes.append('GARANTIDO| Suporte à vida mantido ativo.')

    return acoes


def desligar_nao_essenciais():
    for sub in dados.sistemas['nao_essenciais'].values():
        sub['ativo'] = False


def garantir_suporte_vida():
    for sub in dados.sistemas['suporte_vida'].values():
        sub['ativo'] = True


def exibir_decisoes():
    print()
    for acao in avaliar_regras():
        print(f"  > {acao}")
