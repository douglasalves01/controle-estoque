def calcular_preco_venda(custo_produto, custo_fixo_pct, comissao_venda_pct, imposto_venda_pct, margem_lucro_pct):
"""
Calcula o preço de venda com base nos custos, comissões, impostos e margem de lucro desejada.
Retorna o preço de venda calculado.
"""
if not 0 <= custo_fixo_pct <= 100 or not 0 <= comissao_venda_pct <= 100 or \
 not 0 <= imposto_venda_pct <= 100 or not 0 <= margem_lucro_pct <= 100:
raise ValueError("Percentuais devem estar entre 0 e 100.")

    fatores = (custo_fixo_pct + comissao_venda_pct + imposto_venda_pct + margem_lucro_pct) / 100
    if fatores >= 1:
        raise ValueError("A soma dos percentuais não pode ser igual ou maior que 100%.")

    return custo_produto / (1 - fatores)

## relatórios de vendas/relatório

def classificar*lucro(custo_produto, preco_venda):
"""
Classifica o lucro baseado na diferença entre o preço de venda e o custo do produto.
Retorna uma string com a classificação do lucro.
"""
lucro = preco_venda - custo_produto
if lucro > custo_produto * 0.2:
return "Alto"
elif custo*produto * 0.1 < lucro <= custo*produto * 0.2:
return "Lucro médio"
elif 0 < lucro <= custo*produto * 0.1:
return "Lucro baixo"
elif lucro == 0:  
 return "Equilíbrio"
else:  
 return "Prejuízo"

# Solicitação de entrada e validação

## um post pra salvar isso no banco e um get pra retornar isso pra mostrar na tela de config

custo_produto = float(input("Digite o custo do produto em reais: "))
if custo_produto < 0:
raise ValueError("O custo do produto não pode ser negativo.")

custo_fixo_pct = float(input("Digite o custo fixo/administrativo em porcentagem: "))
comissao_venda_pct = float(input("Digite a comissão de venda em porcentagem: "))
imposto_venda_pct = float(input("Digite o imposto sobre a venda em porcentagem: "))
margem_lucro_pct = float(input("Digite a margem de lucro em porcentagem: "))

preco_venda = calcular_preco_venda(custo_produto, custo_fixo_pct, comissao_venda_pct, imposto_venda_pct, margem_lucro_pct)

print(f"O preço de venda é: R$ {preco_venda:.2f}")
print(f"Classificação do lucro: {classificar_lucro(custo_produto, preco_venda)}")
