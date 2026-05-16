"""
#listas

my_list = []

my_list.append("Willie")

#my_list.remove("Willie")

my_list.append("Alexander")
my_list.append("Juan")
my_list.append("Pedro")
my_list[0] = "Joselito"
my_list.sort()



print(my_list)


#tuplas
my_tuple = ()
my_tuple = "Python","Java","JScript","C#"
print(my_tuple[0])

print(my_tuple)

#sets
my_set = {"willie"}
my_set.add("omar")
my_set.remove("omar")
print(type(my_set))


#diccionarios

my_dict = {1:"Willie",2:"Casimiro"}
my_dict[3] = "Alexander" #insercion
my_dict[1] = "Pedro" #actualizacion
del my_dict[3]  #eliminacion
print(my_dict)
"""

# Agenda Teléfonica
import os
import msvcrt

opcion = 0
agenda = []


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def search_contact():
    value = input("Nombre o Telefono ==> ")
    for contacto in agenda:
        if contacto["name"] == value or contacto ["phone"] == value:
            print(contacto)
            print("Pulsa una tecla para continuar...")
            msvcrt.getch()
            clear_screen()

def add_contact():
    try:
        name = input("Nombre ==> ")
        phone = (input("Telefono ==>"))
        if phone.isnumeric() == True and len(phone) <= 11:

            agenda.append({"name":name.upper(),"phone":phone})
            print("Contacto agregado exitosamente")
            print("Pulsa una tecla para continuar...")
            msvcrt.getch()
            clear_screen()
        else:
            print("Error, no puedes ingresar un numero de telefono con letras o con mas de 11 digitos.")
            print("Pulsa una tecla para continuar...")
            msvcrt.getch()
            clear_screen()
    except(Exception):
            print(Exception)    


def update_contact():
    phone = input("Telefono ==>")
    for contacto in agenda:
        if contacto["phone"] == phone:
            try:
                contacto["phone"] = input("Escriba el nuevo numero de telefono ==> ")
                print("Contacto editado exitosamente")
                print("Pulsa una tecla para continuar...")
                msvcrt.getch()
                clear_screen()
            except(Exception):
                print(Exception)    

def remove_contact():
    phone = input("Telefono ==>")
    for contacto in agenda:
        if contacto["phone"] == phone:
            try:
                del contacto
                print("Contacto eliminado exitosamente")
                print("Pulsa una tecla para continuar...")
                msvcrt.getch()
                clear_screen()
            except(Exception):
                print(Exception)    

while(opcion != 5):
    print("Agenda Teléfonica")
    print("Menú:\n1.Buscar Contacto\n2.Agregar Contacto\n3.Actualizar Contacto\n4.Eliminar Contacto\n5.Salir")
    opcion = int(input("Elija una opción ==> "))
    match opcion:
        case 1:
            clear_screen()
            search_contact()
        case 2:
            add_contact()

        case 3:
            update_contact()
        case 4:
            remove_contact()
        case 5:
            break
print("Gracias por usar nuestra agenda :)")