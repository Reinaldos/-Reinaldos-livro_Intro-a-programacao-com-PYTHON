# Escreva um programa que pergunte a distância que um passageiro 
# deseja percorrer em km. Calcule o preço da passagem, cobrando R$ 0,50 por km 
# para viagens de até de 200 km, e R$ 0,45 para viagens mais longas.
distancia = float(input('Qual a disancia que deseja percorrer em km?\n'))
if distancia <= 200:
    preco = distancia * 0.50
else :
    preco = distancia * 0.45
print('o valor da sua corrida é R$ %3.2f'%preco)
#EU SOU UBER E ESSE PREÇO NUNCA VAI EXISTIR, NÃO PAGA NEM A FUMAÇA DO ESCAPAMENTO! ISSO
#É UM EXEMPLO
