# Exercício 4.8 Escreva um programa que leia dois números e que pergunte qual 
# operação você deseja realizar. Você deve poder calcular a soma (+), subtração (-), 
# multiplicação (*) e divisão (/). Exiba o resultado da operação solicitada
def calculos():
    numero_1 = int(input('digite o primeiro numero\n'))
    numero_2 = int(input('digite o segundo numero\n'))
    operacoes = input('Qual operação deseja executar?\n soma(+),subtração(-),divisão(/) ou multiplicação(*)?\n')
    if "+" in operacoes:
        print('a soma dos numeros é %3d'%(numero_1 + numero_2)) 
        calculos()
    elif '/' in operacoes:
        print(' a divisão dos numeros é %3d'%(numero_1 / numero_2))
        calculos()
    elif '-' in operacoes:
        print(' a subtração dos numeros é %3d'%(numero_1 - numero_2))
        calculos()
    elif '*' in operacoes:
        print(' a multiplicação dos numeros é %3d'%(numero_1 * numero_2))
        calculos()
    else:
        print('você precisa digitar um dos símbolos de operação \n +,-,/ ou *')
        calculos()
calculos()