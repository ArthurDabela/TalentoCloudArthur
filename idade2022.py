#Desenvolva um programa que recebe do usuário nome completo e ano de nascimento que seja entre 1922 e 2021.
#A partir dessas informações, o sistema mostrará o nome do usuário e a idade que completou, ou completará, no ano atual (2022).

#Caso o usuário não digite um número ou apareça um inválido no campo do ano,
# o sistema informará o erro e continuará perguntando até que um valor correto seja preenchido.

rodar = True

while (rodar == True):
    nome = input("Digite seu nome completo: ")
    anoNascimento= int(input("Digite seu ano de nascimento: "))
    if ((anoNascimento >= 1922) and (anoNascimento <= 2021)):
        rodar = False
        print("Seu nome é:", nome, "e completou no ano de 2022", 2022 - anoNascimento, "anos")
    else:
        raise Exception("Ano de nascimento digitado incorretamente!")
