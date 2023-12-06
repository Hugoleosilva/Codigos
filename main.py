horas_por_dia = 8
dias_totais = 15
horas_trabalho = horas_por_dia * dias_totais
custo_hora = 100
custo_total = horas_trabalho * custo_hora
print(custo_total)

capacidade_tanque = 50
no_tanque = 20
custo_litro = 5.03
custo_total_litro = (capacidade_tanque - no_tanque) * custo_litro
print(custo_total_litro)

vendas = 1200.0
meta = 1000.0
salario = 1300.0
if vendas > meta:
    bonus = 250.0
else:
    bonus = 50.0
print(bonus + salario)

vendas = 700.0
meta = 1000

if vendas > meta:
    bonus = 250.0
else:
    bonus = 50.0
print(bonus + salario)

# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

vendas = 1200.0
meta = 1000.0
vendas_empresa = 11000.0
meta_empresa = 10000.0

if vendas > meta and vendas_empresa > meta_empresa:
    bonus = 250.0
else:
    bonus = 50.0
print(bonus)

vendas = 800.0
meta = 1000.0
vendas_empresa = 8000.0
meta_empresa = 10000.0

if vendas > meta and vendas_empresa > meta_empresa:
    bonus = 250.0
else:
    bonus = 50.0
print(bonus)

vendas = 800.0
meta = 1000.0
vendas_empresa = 12000.0
meta_empresa = 10000.0

if vendas > meta and vendas_empresa > meta_empresa:
    bonus = 250.0
else:
    bonus = 50.0
print(bonus)


//crie uma funcao que some dois numeros e faca a media
