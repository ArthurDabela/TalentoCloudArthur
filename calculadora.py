#Faça uma função calculadora de dois números com três parâmetros: os dois primeiros serão os números da operação 
#e o terceiro será a entrada que definirá a operação a ser executada. Considera a seguinte definição:
#1. Soma
#2. Subtração
#3. Multiplicação
#4. Divisão

#Caso seja inserido um número de operação que não exista, o resultado deverá ser 0.

def calculadora(num1, num2, tipoOperacao):
    if (tipoOperacao == 1):
        total = num1 + num2
    elif (tipoOperacao == 2):
        total = num1 - num2
    elif (tipoOperacao == 3):
        total = num1 * num2
    elif (tipoOperacao == 4):
        total = num1 / num2 
    else:
        total = 0
    print("O total foi: ", total)

print("=== Calculadora ===")
print("1 - Soma")
print("2 - Subtração")
print("3 - Multiplicação")
print("4 - Divisão")
tipoOperacao = int(input("Digite qual operação deseja fazer: "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
calculadora(num1, num2, tipoOperacao)