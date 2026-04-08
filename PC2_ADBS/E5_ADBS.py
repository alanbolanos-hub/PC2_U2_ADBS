# Est. Alan Bolaños
salario_diario = 500
dias_trabajados = 22

salario_bruto = salario_diario * dias_trabajados

descuento_seguro = salario_bruto * 0.10
descuento_ahorro = salario_bruto * 0.05

salario_neto = salario_bruto - (descuento_seguro + descuento_ahorro)

print("Salario bruto:", salario_bruto)
print("Descuento por seguro:", descuento_seguro)
print("Descuento por ahorro:", descuento_ahorro)
print("Salario neto:", salario_neto)