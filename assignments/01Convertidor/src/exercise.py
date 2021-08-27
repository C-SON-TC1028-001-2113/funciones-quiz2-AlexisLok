# Escribe tus funciones abajo de esta línea
def pies_cm(pies):
    cm = pies * 30.48
    print(cm)

def pulgadas_cm(inch):
    cm = inch * 2.54
    print(cm)

def yardas_cm(yardas):
    cm = yardas * 91.44
    print(cm)

def main():
    # Escribe tu código abajo de esta línea
    print("1. pies a cm, 2. pulgadas a cm, 3. yardas a cm")
    opcion = int(input("Introduce una opcion: "))

    # Aqui se realiza el analisis de la canidad ingresada
    cantidad = int(input("Introduce la cantidad: ")) 
    if cantidad > 0:
        pass
    else:
        print("Error")
        opcion = 0
        pass

    # Aqui comienza las opciones para las funciones
    if opcion == 1:
        pies_cm(cantidad)
        pass
    elif opcion == 2:
        pulgadas_cm(cantidad)
        pass
    elif opcion== 3:
        yardas_cm(cantidad)
        pass
    else:
        print("Error")
        pass
        
if __name__ == '__main__':
    main()
