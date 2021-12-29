# Exercício 4.3 Escreva um programa que leia três números e que imprima o maior 
# e o menor.
numero1 = int(input('digite o primeiro numero   '))
numero2 = int(input('digite o segundo numero  '))
numero3 = int(input('digite o terceiro numero '))
if (numero1 > numero2) and (numero1 > numero3):
    print('o maior numero é %d'%numero1)
elif (numero1 < numero2) and (numero1 < numero3):
    print('o menor numero é %d'%numero1)
if (numero2 > numero3) and (numero2> numero1):
    print('o maior numero é %d'%numero2)
elif (numero2 < numero3) and (numero2 < numero1):
    print('o menor numero é %d'%numero2)
if (numero3 > numero2) and (numero3 > numero1):
    print('o maior numero é %d'%numero3)
elif (numero3 < numero2) and (numero3 < numero1):
    print('o menor numero é %d'%numero3)


