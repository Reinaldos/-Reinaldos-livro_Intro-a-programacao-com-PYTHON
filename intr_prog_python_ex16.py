# Faça um programa que solicite o preço de uma mercadoria e o
#  percentual de desconto. Exiba o valor do desconto e o preço a pagar.
mercadoria = float(input('Qual é o preço da mercadoria? \n'))
desconto = float(input('Qual o desconto em porcentagem? \n'))
percentualdedesconto = mercadoria*desconto/100
mercadoriacomdesconto = mercadoria-percentualdedesconto
print('o valor do desconto é %3.3f' % percentualdedesconto)
print('o valor da mercadoria com desconto é %3.3f' %mercadoriacomdesconto)