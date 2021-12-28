#Exercício 3.4 Escreva uma expressão para determinar se uma pessoa deve ou não 
# pagar imposto. Considere que pagam imposto pessoas cujo salário é maior que 
# R$ 1.200,00


def pobre_ou_rico(): 
    salario =float (input ("Digite aqui seu salário com os centavos   "))
    if salario < 1000:
        print("Você é mendigo, não precisa pagar imposto use seu dinheiro para comer!")
        pobre_ou_rico()
    elif salario > 1.200:
        print("Você precisa pagar imposto")
        pobre_ou_rico()
    else:
        print("Você é mendigo, não precisa pagar imposto use seu dinheiro para comer!")
        pobre_ou_rico()
pobre_ou_rico()