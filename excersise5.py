"""
#operaciones con caracteres

string1 = "Hola"
string2 = "Python"

#concatenacion
print(string1 + string2)


#repeticion
print(string1*5)

# Indexacion
print(string1[0])

#Longitud
print(len(string1))

#Slicing(porcion)
print(string1[1:3])

#Busqueda
print("s" in string1)

#reemplazo
print(string1.replace("H","Y"))

#Division
print(string2.split("t"))

#Eliminacion de espacios al principio y al final
print(string2.strip())

#Busqueda al principio y al final
print(string2.startswith("P"))
print(string2.endswith("n"))

#busqueda de posicion
print(string2.find("n"))

text1 = "salas"
text2 = "salas"

if(text2[::-1] == text1):
    print("Es palindromo")
else:
    print("No es palindromo")

    
text1 = ''.join(sorted("ropa"))
text2 = ''.join(sorted("paro"))

if  text1 == text2:
    print("Es anagrama")
else:
    print("No es anagrama")
"""
