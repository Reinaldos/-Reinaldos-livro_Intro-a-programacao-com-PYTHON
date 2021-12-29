# Faça um programa que calcule o aumento de um salário. Ele deve 
# solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento 
# e do novo salário
salario = float(input('digite aqui o valor do salário R$ '))
porcentagem_de_aumento = float(input('digite aqui a porcentagem de aumento  '))
novosalário = salario + (salario * porcentagem_de_aumento/100)
valordoaumento = novosalário-salario
print('O VALOR DO AUMENTO É DE %d'% valordoaumento)
print('portanto o novo salário fica %d'% novosalário)