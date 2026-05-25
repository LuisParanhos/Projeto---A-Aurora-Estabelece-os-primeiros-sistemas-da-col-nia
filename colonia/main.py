import dados
import decisoes
import energia
import previsao


def titulo(texto):
    print(f"\n{'='*52}")
    print(f"  {texto}")
    print('='*52)


def secao(texto):
    print(f"\n  -- {texto} --")


def exibir_status_colonia():
    titulo("STATUS DA COLÔNIA")
    dados.exibir_colonia()
    secao("Sistemas")
    dados.exibir_sistemas()


def exibir_resultados():
    titulo("ANÁLISE ATUAL")
    secao("Energia")
    energia.exibir_analise()
    secao("Previsão eólica")
    previsao.exibir_previsao()
    secao("Decisões do sistema")
    decisoes.exibir_decisoes()


def exibir_exemplos():
    titulo("EXEMPLOS")

    secao("Previsões para diferentes velocidades de vento")
    print(f"\n  {'Vento (m/s)':<15} {'Energia prevista (kW)'}")
    print("  " + "-" * 35)
    for vento in [5, 10, 15, 20, 25]:
        estimativa = previsao.prever_energia(vento)
        print(f"  {vento:<15} {estimativa}")

    secao("Análise para diferentes cenários de geração e consumo")
    print()
    exemplos = [
        {'geracao': 50, 'consumo': 60},
        {'geracao': 60, 'consumo': 50},
        {'geracao': 55, 'consumo': 55},
        {'geracao': 40, 'consumo': 65},
    ]
    for exemplo in exemplos:
        resultado = energia.analisar_consumo(**exemplo)
        print(resultado)


def cenario_critico():
    titulo("CENÁRIO CRÍTICO — energia cai para 15%")
    dados.atualizar_dado('energia', 15)
    secao("Decisões")
    decisoes.exibir_decisoes()
    secao("Estado dos sistemas após decisões")
    dados.exibir_sistemas()


if __name__ == "__main__":
    titulo("SIMULAÇÃO DA COLÔNIA INTELIGENTE")
    exibir_status_colonia()
    exibir_resultados()
    exibir_exemplos()
    cenario_critico()
    titulo("FIM DA SIMULAÇÃO")
