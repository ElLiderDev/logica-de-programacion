"""
Programa de gestion de ventas
"""
import os
import subprocess


def limpiar_pantalla():
    input("Pulse Enter para continuar...")
    comando = "cls" if os.name == "nt" else "clear"
    subprocess.run(comando, shell=True)

def add_product():
    products = []
    products.append(input("Introduzca el nombre del producto ==> "))
    products.append(input("Introduzca la cantidad ==> "))
    products.append(input("Introduzca el precio ==> "))
    return products
try:
    while(True):
        file_name = "Products.txt"

        print("Bienvenidos a gestion de ventas \n" \
        "1. Añadir Producto \n" \
        "2. Consultar Producto \n" \
        "3. Actualizar Producto \n" \
        "4. Eliminar Producto \n" \
        "5. Salir")
        option = input("Elija una opción ==> ")

        match(option):
            case '1':
                products = add_product()
                with open(file_name,"a") as file:
                        file.write(f"{str(products)}\n")
                print("Producto añadido correctamente")
                limpiar_pantalla()


            case '2':
                product = input("Introduzca el nombre del producto ==> ")
                with open(file_name, "r", encoding="utf-8") as file:
                    for numero_linea, linea in enumerate(file, start=1):
                        if product in linea:
                            print(f"{linea.strip()}")
                            limpiar_pantalla()
                            exist = True
                        else:
                            exist = False
                if exist == False:
                    print("El producto no existe") 
                    limpiar_pantalla()

            case '3':
                product = input("Introduzca el nombre del producto ==> ")
                with open(file_name, "r") as file:
                    lines = file.readlines()

                with open(file_name,'w') as file:
                    for line in lines:
                        if product in line:
                            products = add_product()
                            file.write(str(products))
                        else:
                            file.write(line)
            case '4':
                product = input("Introduzca el nombre del producto ==> ")
                with open(file_name, "r") as file:
                    lines = file.readlines()

                with open(file_name,'w') as file:
                    for line in lines:
                        if product not in line:
                            file.write(line)
                        else:
                            print("Producto eliminado correctamente")
                            limpiar_pantalla()
    

            case '5':
                os.remove(file_name)
                break
except Exception as e:
    print(e)
