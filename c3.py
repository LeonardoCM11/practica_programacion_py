print("Bienvenido a la calculadora un poco mas avanzada papure")

operacion = input("Ingrese la operacion a ejecutar ejemplo:\n+ | - | * | / \no si gusta salir escriba exit\n")
x = float(input("Ingrese su primer numero \n"))
y = float(input("Ingrese su segundo numero \n"))


while operacion != "exit":

#    operacion = input("Ingrese la operacion a ejecutar ejemplo:\n+ | - | * | / \no si gusta salir escriba exit\n")
 #   x = float(input("Ingrese su primer numero \n"))
  #  y = float(input("Ingrese su segundo numero \n"))
    

    if operacion == "+":
        print(x+y)
    elif operacion == "-":
            print(x-y)
    elif operacion == "*":
            print(x*y)
    elif operacion == "/" and x!=0 or y!=0:
            print(x/y)    
    else:
        print("Ingrese una opcion valida\n")
          