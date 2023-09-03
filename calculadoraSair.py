#Faça uma função calculadora que os números e as operações serão feitas pelo usuário.
#O código deve ficar rodando infinitamente até que o usuário escolha a opção de sair. No início, o programa mostrará a seguinte lista de operações:

#1: Soma
#2: Subtração
#3: Multiplicação
#4: Divisão
#0: Sair

#Digite o número para a operação correspondente e caso o usuário introduza qualquer outro, o sistema deve mostrar a mensagem “Essa opção não existe” e voltar ao menu de opções.

#Após a seleção, o sistema deve pedir para o usuário inserir o primeiro e segundo valor, um de cada. Depois precisa executar a operação e mostrar o resultado na tela.
# Quando o usuário escolher a opção “Sair”, o sistema irá parar.

#É necessário que o sistema mostre as opções sempre que finalizar uma operação e mostrar o resultado. 

def calculadora(num1, num2, tipoOperacao):
    if (tipoOperacao == 1):
        total = num1 + num2
        print("O total foi: ", total)
    elif (tipoOperacao == 2):
        total = num1 - num2
        print("O total foi: ", total)
    elif (tipoOperacao == 3):
        total = num1 * num2
        print("O total foi: ", total)
    elif (tipoOperacao == 4):
        total = num1 / num2 
        print("O total foi: ", total)
    else:
        print("Essa opção não existe")

tipoOperacao = 1
while(tipoOperacao != 0):
    print("=== Calculadora ===")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("0 - Sair")
    tipoOperacao = int(input("Digite qual operação deseja fazer: "))
    if (tipoOperacao == 0):
        break
    num1 = int(input("Digite o primeiro número: "))
    num2 = int(input("Digite o segundo número: "))
    calculadora(num1, num2, tipoOperacao)