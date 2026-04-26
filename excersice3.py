def two_values(value1,value2):
    contador = 0
    for num in range(1,101):
        if num % 3 == 0 and num % 5 == 0:
            print(value1,value2)
        elif num % 3 == 0:
            print(value1)
        elif num % 5 == 0:
            print(value2)
        else:
            print(num)
            contador +=1
    return contador

contador = two_values("Fizz","Buzz")
print(contador)