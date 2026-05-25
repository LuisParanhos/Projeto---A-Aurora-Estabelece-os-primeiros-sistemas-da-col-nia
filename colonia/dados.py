colonia = {
    'energia': 50,
    'consumo': 60,
    'vento': 9,
    'clima': 'nublado'
}

sistemas = {
    'energetico': {
        'solar':  {'capacidade': 50, 'ativo': True},
        'eolico': {'capacidade': 40, 'ativo': True}
    },
    'suporte_vida': {
        'oxigenio':    {'ativo': True, 'prioridade': 1},
        'temperatura': {'ativo': True, 'prioridade': 1}
    },
    'nao_essenciais': {
        'iluminacao_extra': {'ativo': True,  'prioridade': 3},
        'entretenimento':   {'ativo': False, 'prioridade': 4}
    },
}

historico_vento   = [8, 10, 12, 9, 7]
historico_energia = [45, 50, 55, 60, 65]


def obter_dados(valor):
    return colonia[valor]


def atualizar_dado(dado, valor):
    colonia[dado] = valor


def exibir_colonia():
    print("\n  Dado            Valor")
    print("  " + "-" * 25)
    for chave, valor in colonia.items():
        print(f"  {chave:<16} {valor}")


def exibir_sistemas():
    for nome_grupo, subsistemas in sistemas.items():
        print(f"\n  [{nome_grupo.upper()}]")
        for nome_sub, atributo in subsistemas.items():
            status     = "LIGADO  " if atributo['ativo'] else "DESLIGADO"
            prioridade = atributo.get('prioridade', '-')
            capacidade = atributo.get('capacidade', '-')
            print(f"    └─ {nome_sub:<20} {status}  prioridade={prioridade}  capacidade={capacidade}")
