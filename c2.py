print("bienvenido a la calculadora que de menos ya calcula una que otra mamada con 2 num xd")

x = float(input("Ingrese su primer numero de favor invezil\n"))
y = float(input("Ingrese su segundo numero de favor invezil\n"))

operacion = input("Ingrese la operacion a realizar \n+ - * / \n")

if operacion == "+" :
    print(x + y) 

elif operacion == "-":
    print(x - y)

elif operacion == "*":
    print(x * y)

elif operacion == "/":
    print(x / y)

else:
    print("Seleccione una operacion valida invezil")