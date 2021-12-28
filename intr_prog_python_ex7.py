# Exercício 3.6 Escreva uma expressão que será utilizada para decidir se um aluno foi 
# ou não aprovado. Para ser aprovado, todas as médias do aluno devem ser maiores 
# que 7. Considere que o aluno cursa apenas três matérias, e que a nota de cada uma 
# está armazenada nas seguintes variáveis: matéria1, matéria2 e matéria
def dados_do_meliante():
    aluno = input("digite o nome do meliante!   ")
    materia1 = int (input("digite a primeira nota do meliante  "))
    materia2 = int (input("digite a segunda nota do meliante  "))
    materia3 = int (input("digite a terceira nota do meliante  "))
    soma = materia1+materia2+materia3
    media = soma / 3
    if  media >= 7:
       print("esse vagabundo passou de ano!")
       dados_do_meliante()
    else:
       print("coloca esse safado pra estudar!")
       dados_do_meliante()
dados_do_meliante()




