lista = []

def mostrar_estudiante():
    print("\nNOMBRE", "edad", "nota")
    for nombre, edad, nota in lista.items():
        print(f"{nombre}: {edad}: {nota}")
        
while True:                                   #el while permite que el menu vuelva aparecer cuando termine un a ejecucion
    print("\n========MENU PRINCIPAL========")
    print("1. Agregar estudiante")
    print("2. Buscar estudiante")
    print("3. Eliminar estudiante")
    print("4. Actualizar estado")
    print("5. Mostrar estudiante")
    print("6. salir")

    
    try:                                                #el try except para que no caiga el sistema en caso de error
        opcion = int(input("elige una opcion (1-6): "))
        
        if opcion == 1:
           nombre = input("ingresa el nombre del estudiante: ")   #el input para engresar texto
           edad = int(input("ingresa la edad del estudiante: "))  #el int para numero intero
           nota = float(input("ingresa la nota del estudiante: ")) #el float para ingresar numero decimal
           lista.append({"nombre", "edad", "nota"})
           if nota >= 4:
               print("el estudiante ha aprobado")
           else:
               print("el estudiante ha reprobado")
           print("estudiante ha sido agregado correctamente")
        elif opcion == 2:
           nombre = input("ingresa el nombre del estudiante a buscar: ")
           if nombre in lista:
              print(f"el nombre a buscar es: {nombre}")
           else:
            print("no se encontraron el estudiante")
        elif opcion == 3:
           nombre = input("ingresa el nombre del estudiante a eliminar: ")
           if nombre in lista:
              lista.remove(nombre)
              print("el nombre del estudiante ha sido eliminado correctamente")
           else:
              print("el nombre del estudiante no fue encontrado")
        elif opcion == 4:
           nombre = input("ingresa el nombre del estudiante a actualizar: ")
           if nombre in lista:
              edad = int(input("ingresa la edad del estudiante: "))
              nota = float(input("ingresa la nota del estudiante: "))
              for estudiante in lista:
                print("estudiante ha sido actualizado correctamente")
        elif opcion == 5:
           if not lista:
              print("la lista de estudiante esta bacia")
           else:
              mostrar_estudiante()
        elif opcion == 6:
           print("salir del programa")
           print("gracias por usar el programa")
        else:
            print("opcion invalida")
    except ValueError:
        print("error: ingresa un valor valido")
        
        
