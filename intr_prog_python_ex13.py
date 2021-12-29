# Escreva um programa que leia um valor em metros e o exiba convertido em milímetros
metros = float(input('digite o tamanho em metros '))
centimetros = metros*100
milimetros = centimetros*10
print('Esse tamano em metros convertido para centimetros é %3.2f e para milimetros é %3.21f'%(centimetros,milimetros))