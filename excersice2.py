"""
Operadores
"""


#Operadores Aritmeticos
print(5+5)
print(5-3)
print(5*2)
print(5/2)
print(10%2)
print(10**2)
print(10 // 3)


#Operadores de comparacion
print(10 == 10)
print(10 != 2)
print(10 > 20)
print(10 < 20)
print(10 >= 10)
print(20 <= 30)



#Operadores Logicos
True and True
False or True
not True

#Operadores de asignacion
my_number = 1
my_number +=1
my_number -= 1
my_number *= 1
my_number /= 1
my_number %= 1
my_number **= 1
my_number //=1

#Operadores de identidad
my_new_number = my_number
print(my_number is my_new_number)
print(my_number is not my_new_number)

#Operadores de pertenencia
print("u" in "moure")
print("u" not in "moure")

#Operadores de bit




#Ejercicio

for number in range(10,56):
    if(number % 2 ==0):
        if number != 16 and number % 3 !=0:
            print(number)