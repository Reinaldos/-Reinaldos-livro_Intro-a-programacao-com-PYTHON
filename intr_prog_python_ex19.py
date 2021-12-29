# Escreva um programa que pergunte a quantidade de km percorridos 
# por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais 
# o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60 por 
# dia e R$ 0,15 por km rodado.
km = float(input('quantos kilometros foram percorridos? '))
dias =  float(input('por quantos dias o carro foi alugado ' ))
preçokm = km*0.15
preçodia = dias*60.00
valortotal = preçodia+preçokm
print('pelos km percorridos você pagará R$ %2.2f'%preçokm)
print('pelos dias você pagará R$ %2.2f'%preçodia)
print('o total pelo aluguel do carro é R$ %2.2f'%valortotal)