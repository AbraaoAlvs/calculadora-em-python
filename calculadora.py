def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

while True:
    print("Selecione a operação.")
    print("1.Somar")
    print("2.Subtrair")
    print("3.Multiplicar")
    print("4.Dividir")
    print("0.Sair")

    escolha = input("Digite sua escolha (0/1/2/3/4): ")

    if escolha == '0':
        print("Saindo...")
        break

    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    if escolha == '1':
        print(num1,"+",num2,"=", add(num1,num2))

    elif escolha == '2':
        print(num1,"-",num2,"=", subtract(num1,num2))

    elif escolha == '3':
        print(num1,"*",num2,"=", multiply(num1,num2))

    elif escolha == '4':
        print(num1,"/",num2,"=", divide(num1,num2))

    else:
        print("Opção inválida")

    input("Pressione qualquer tecla para continuar...")
    print("\n")
