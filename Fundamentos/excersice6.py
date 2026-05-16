"""
Valor y referencia
"""

#Tipos de dato por valor

my_int_a = 10
my_int_b = my_int_a
print(my_int_a)
print(my_int_b)


#Tipos de datos por referencia

my_list_a = [10,20]
my_list_b = my_list_a
my_list_b.append(30)
print(my_list_a)
print(my_list_b)
