# u Listagem 3.20 – Cálculo de bônus por tempo de serviço
anos = int(input("Anos de serviço: "))
valor_por_ano = float(input("Valor por ano: "))
bônus = anos * valor_por_ano
print("Bônus de R$ %5.2f" % bônus)