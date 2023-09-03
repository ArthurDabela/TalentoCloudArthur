#Precisamos imprimir um número para cada andar de um hotel de 20 andares. Porém, o dono do hotel é supersticioso e optou por não ter um 13ro andar.
#
#Escreva um código que imprima todos os números exceto o número 13.
#Escreva mais dois códigos que resolvam o mesmo problema, mas dessa vez usando os outros dois tipos de laços de repetição aprendidos.
#
#Como desafio, imprima eles em ordem decrescente (20, 19, 18...)

andaresHotel = 20
for i in range(andaresHotel):
    if ((i + 1) != 13):
        print("Andar n°: ", i + 1)

i = 0
while (i < 20):
    if ((i + 1) != 13):
        print("Andar n°: ", i + 1)
    i = i + 1

i = 19
while (i >= 0):
    if ((i + 1) != 13):
        print("Andar n°: ", i + 1)
    i = i -1