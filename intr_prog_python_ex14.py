# Escreva um programa que leia a quantidade de dias, horas, minutos 
# e segundos do usuário. Calcule o total em segundos.
dias = int(input('digite a quantidade de dias '))
horas = int(input('digite a quantidade de horas '))
minutos = int(input('digite a quantidade de minutos '))
segundos = int(input('digite a quantidade de segundos '))

diasemsegundos = dias*24*60*60
horasemsegundos = horas*60*60
minutosemsegundos = minutos*60
total = diasemsegundos+horasemsegundos+minutosemsegundos+segundos
print('O total de tudo isso é %d segundos' % total )