# Exercício 4.9 Escreva um programa para aprovar o empréstimo bancário para 
# compra de uma casa. O programa deve perguntar o valor da casa a comprar, o 
# salário e a quantidade de anos a pagar. O valor da prestação mensal não pode ser 
# superior a 30% do salário. Calcule o valor da prestação como sendo o valor da 
# casa a comprar dividido pelo número de meses a pagar.
valor_da_casa = float(input('Qual o valor da casa em questão?\n'))
salario = float(input('Qual o seu salário?\n'))
anos = int(input('Em quantos anos pretende pagar?\n'))
meses = anos*12
valor_da_prestacao = valor_da_casa / meses
if valor_da_prestacao > (salario/100)*30:
    print('o valor da prestação corresponde a mais de 30% \n do seu salário')
else:
    print('O valor da prestação é \nR$%3.3f'%valor_da_prestacao)