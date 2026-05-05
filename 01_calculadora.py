numero1=float(input("Ingrese un numero: "))
accion=input("Ingrese la accion a realizar: ")
numero2=float(input("Ingrese otro numero: "))
if accion == "/":
    if numero2 != 0:
        resultado=numero1 / numero2
        print ("El resultado es:",resultado)
    else:
        print("No se puede dividir un numero por 0.")

elif accion == "+":
    resultado=numero1 + numero2
    print("El resultado es:",resultado)
elif accion == "-":
    resultado= numero1 - numero2
    print("El resultado es:", resultado)
elif accion == "*":
    resultado = numero1 * numero2
    print("El resultado es:", resultado)


else:
    print("La accion no es valida. Por favor ingrese: *,+,- o /.") 
