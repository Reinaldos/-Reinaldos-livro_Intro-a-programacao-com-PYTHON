# Escreva um programa para calcular a redução do tempo de vida de 
# um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos 
# ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, 
# calcule quantos dias de vida um fumante perderá. Exiba o total em dias.
cigarrosdia = float(input('quantos cigarro tu fuma por dia meu cumpadi?'))
cigarrosano = float(input('e há quantos anos tu fuma?'))
minutoperdido = 10 * cigarrosdia
horaperdida = minutoperdido * 60
diasperdidos = horaperdida / 24
anosperdidos = diasperdidos/360
print('Voce fumou por %2.2d horas \n %2.2d dias \n e perdeu \n %2.2d anos com isso'%(horaperdida,diasperdidos,anosperdidos))


