# Listagem 3.12 – Exemplo de composição de string
nome = "João"
idade = 22
grana = 51.34
print("%s tem %d anos e R$%f no bolso." % (nome, idade, grana))
# João tem 22 anos e R$51.340000 no bolso.
print("%12s tem %3d anos e R$%5.2f no bolso." % (nome, idade, grana))
# João tem 22 anos e R$51.34 no bolso.
print("%12s tem %03d anos e R$%5.2f no bolso." % (nome, idade, grana))
# João tem 022 anos e R$51.34 no bolso.
print("%-12s tem %-3d anos e R$%-5.2f no bolso." % (nome, idade, grana))
# João tem 22 anos e R$51.34 no bolso.