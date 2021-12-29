# Escreva um programa que calcule o tempo de uma viagem de carro. 
# Pergunte a distância a percorrer e a velocidade média esperada para a viagem.
distancia = float(input('Qual a distância da viagem em km?\n '))
velocidade = float(input('Qual a velocidade média em kmh?\n '))
tempo_estimado = distancia/velocidade
print('O tempo estimado para éssa viagem é de %2.2f horas' % tempo_estimado)