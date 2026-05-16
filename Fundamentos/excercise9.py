"""
Clases


class Willie:
    def __init__(self,name:str,surname:str,age:int):
        self.name = name
        self.surname = surname
        self.age = age

    def print_data(self):
        print(self.name,self.surname,self.age)

willie = Willie("Willie","Casimiro",25)
willie.print_data()


class Stack:
    def __init__(self):
        stack = list()
        self.stack = stack

    def add(self,value):
        self.stack.append(value)
        print(self.stack)

    def remove(self,value):
        self.stack.pop(value)
        print(self.stack)
    
    def stacklen(self):
        print(len(self.stack))
    
stack = Stack()
stack.add("Blanca nieves")
stack.add("Cenicientas")
stack.stacklen()
stack.remove(1)



class Queue:
    def __init__(self):
        queue = list()
        self.queue = queue

    def add(self,value):
        self.queue.append(value)
        print(self.queue)

    def remove(self,value):
        self.queue.remove(value)
        print(self.queue)

    def len(self):
        print(len(self.queue))

queue = Queue()
queue.add("Manuel 30")
queue.add("Fernando")
queue.add("La Piri")
queue.add("Pajaro jugando voleiball")
queue.remove("La Piri")
queue.remove("Manuel 30")
queue.len()
"""


