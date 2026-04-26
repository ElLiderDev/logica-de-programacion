"""
Recursividad


def print_100_to_0(n:int):
    if n >= 0:
        print(n)
        print_100_to_0(n-1)

print_100_to_0(100)



"""

def factorial(n:int) -> int:
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)




print(factorial(10))


def fibonacci(prev,next,contador):
    if contador <=10:
            if contador == 0:
                print(next)
                contador +=1
                fibonacci(prev,next+1,contador)
            else:   
                print(next)  
                cola = next  
                next = next + prev
                prev = cola 
                contador +=1
                fibonacci(prev,next,contador)
fibonacci(0,0,0)
    