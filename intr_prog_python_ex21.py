# Escreva um programa que pergunte a velocidade do carro de um 
# usuário. Caso ultrapasse 80 km/h, exiba uma mensagem dizendo que o usuário 
# foi multado. Nesse caso, exiba o valor da multa, cobrando R$ 5 por km acima de 
# 80 km/h
velocidade = float(input('qual a velocidade do seu carro?\n'))
if velocidade > 80:
    velocidade = (velocidade - 80)*5
    print('você foi multado em R$ %3.2f'%(velocidade) )
else:
    print ('relaxa dessa vez voce estava abaixo')
