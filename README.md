# Sistema Inteligente da Colônia

Projeto desenvolvido para FIAP - A Aurora Estabelece Os Primeiros Sistemas da Colônia .
O sistema simula o gerenciamento de uma colônia, controlando energia, tomando decisões automáticas e prevendo geração eólica,
todo o trabalho está estruturado em diferentes pastas para manter cada respectiva função separada, priorizando a organização.

---

## Como rodar

Só precisa do Python instalado. Sem bibliotecas externas.

```bash
python main.py
```

---

## Arquivos

- `dados.py` — onde ficam todos os dados da colônia (estado, sistemas e histórico)
- `decisoes.py` — regras de decisão automática baseadas no estado atual
- `energia.py` — compara geração e consumo e dá um diagnóstico
- `previsao.py` — estima a energia gerada com base na velocidade do vento
- `main.py` — chama todos os módulos e exibe os resultados

---

## Como os dados foram organizados

O estado atual da colônia fica em um dicionário simples, utilizamos dados fixos para o trabalho:

```python
colonia = {
    'energia': 50,
    'consumo': 60,
    'vento': 9,
    'clima': 'nublado'
}
```

Os sistemas da colônia ficam em um dicionário, representando a hierarquia entre grupos e subsistemas. O histórico de vento e energia fica em duas listas paralelas, usadas para calcular a previsão.

---

## Regras de decisão

As regras são avaliadas em ordem no `decisoes.py`:

- Se energia < 20%: desliga sistemas não essenciais imediatamente
- Se energia < 50% e consumo > 60%: ativa modo economia
- Se energia < 50%: emite aviso para reduzir consumo
- Se clima for nublado ou tempestade: prioriza geração eólica
- Em qualquer situação: suporte à vida é sempre mantido ativo

---

## Previsão de energia

Usamos regressão linear simples, calculada manualmente com a fórmula de mínimos quadrados. A ideia é ajustar uma reta entre os dados históricos de vento e energia, e usar para estimar os valores futuros.

```
energia = a * vento + b
```

---

## Análise de energia

O módulo compara a geração total dos sistemas ativos com o consumo atual e classifica em quatro situações: crítico, alerta, equilibrado ou excedente. Em caso de excedente, o sistema sugere armazenar a energia.
