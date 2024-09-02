import json

# Exemplo de faturamento diário em formato JSON
faturamento_mensal_json = '''
[
    {"dia": 1, "valor": 22174.1664},
    {"dia": 2, "valor": 24537.6698},
    {"dia": 3, "valor": 26139.6134},
    {"dia": 4, "valor": 0.0}, # Fim de semana
    {"dia": 5, "valor": 0.0}, # Fim de semana
    {"dia": 6, "valor": 26742.6612},
    {"dia": 7, "valor": 0.0}, # Feriado
    {"dia": 8, "valor": 42889.2258},
    {"dia": 9, "valor": 46251.174},
    {"dia": 10, "valor": 11191.4722}
    # Continue com os valores dos dias restantes do mês
]
'''

faturamento_mensal = json.loads(faturamento_mensal_json)

valores = [dia["valor"] for dia in faturamento_mensal if dia["valor"] > 0]

menor_faturamento = min(valores)
maior_faturamento = max(valores)
media_mensal = sum(valores) / len(valores)
dias_acima_da_media = sum(1 for valor in valores if valor > media_mensal)

print(f"Menor faturamento: R${menor_faturamento:.2f}")
print(f"Maior faturamento: R${maior_faturamento:.2f}")
print(f"Número de dias com faturamento acima da média: {dias_acima_da_media} dias")