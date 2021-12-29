# # Exercício 3.8 Escreva um programa que leia um valor em metros e o exiba convertido em milímetros.
metros = float(input('digite um valor em metros  '))
centimetros = metros*100
print ("a conversão dos metros em centimetros resultou em %4.2f centimetros" % (centimetros))

#podemos fazer varios tipos de conversores usando a mesma técnica, não está no livro, 
# no entanto o código abaixo é um conversor de minutos em segundos

# minutos = float(input('digite o tempo em minutos e segundos sem o zero  ' ))
# segundos =  minutos * 60
# print ("a conversão dos minutos em segundos resultou em %4.2f segundos" % (segundos))