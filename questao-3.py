import json
import random

# 3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne:
# • O menor valor de faturamento ocorrido em um dia do mês;
# • O maior valor de faturamento ocorrido em um dia do mês;
# • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.

# IMPORTANTE:
# a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal;
# b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;


# Ler os dados de faturamento diário de um arquivo JSON
with open('dados.json', 'r') as f:
    faturamento = json.load(f)

# Lista que recebe os valores
valores = []

for items in faturamento:
    valores.append(items['valor'])

# Calcular a média mensal de faturamento, ignorando os dias sem faturamento
dias_com_faturamento = [f for f in valores if f != 0]
media_mensal = sum(dias_com_faturamento) / len(dias_com_faturamento)

# Calcular o menor e o maior valor de faturamento
menor_faturamento = min(dias_com_faturamento)
maior_faturamento = max(dias_com_faturamento)

# Contar o número de dias em que o valor de faturamento diário foi superior à média mensal
dias_acima_da_media = len([f for f in valores if f > media_mensal])

# Imprimir os resultados
print(f'Menor faturamento: R${menor_faturamento:,.2f}')
print(f'Maior faturamento: R${maior_faturamento:,.2f}')
print(f'Média Mensal {media_mensal:,.2f}')
print(f'Número de dias com faturamento acima da média mensal: {dias_acima_da_media} dias')