import json
import random

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

faturamento_diario = []
for i in range(31):
    if i < 5 or i > 25:  # simula dias sem faturamento (finais de semana e feriados)
        faturamento_diario.append(0)
    else:
        faturamento_diario.append(random.uniform(1000, 5000))  # simula faturamento diário aleatório entre R$1000 e R$5000

# Inserindo dados no faturamento.json
with open('faturamento.json', 'w') as f:
    json.dump(faturamento_diario, f)

# Ler os dados de faturamento diário de um arquivo JSON
with open('faturamento.json', 'r') as f:
    faturamento = json.load(f)

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(faturamento)
maior_faturamento = max(faturamento)

# Calcular a média mensal de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [f for f in faturamento if f > 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Contar o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = sum(1 for f in faturamento if f > media_mensal)

# Imprimir os resultados
print(f'Menor faturamento: R${menor_faturamento:.2f}')
print(f'Maior faturamento: R${maior_faturamento:.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media}')