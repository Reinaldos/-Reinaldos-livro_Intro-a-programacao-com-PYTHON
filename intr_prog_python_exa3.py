#Listagem 3.11 – Exemplos de composição com números decimais
print("%5f" % 5)
#5.000000
# O primeiro indica o tamanho total em caracteres a reservar; e o 
# segundo, o número de casas decimais. Assim, %5.2f diz que estaremos imprimindo 
# um número decimal utilizando cinco posições, sendo que duas são para a parte 
# decimal
print("%5.2f" % 5)
# 5.00
print("%10.5f" % 5)
#5.00000
print("%s tem %d anos e apenas R$%5.2f no bolso" % ("João", 22, 51.34))
