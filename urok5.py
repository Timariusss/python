
x = 10 
print(type(x)) 
print(dir(x))
print(id(x))

def add(a, b):

    return a + b

print(type(add)) 
print(dir(add))
print(id(add))
help(add)
print(add.__dict__)

import math
print(type(math)) 
print(dir(math))
print(id(math))
help(math)
print(math.pow(x = 2, y = 3))

print("*" * 50)
import requests
print(type(requests)) 
print(dir(requests))
print(id(requests))
help(requests)


class Person:
    species = "human" 
    def __init__(self, name):
        self.name = name 
    def greet(self):
        print(f"Hello, {self.name}")  

print(type(Person)) 
print(dir(Person))
print(id(Person))
help(Person)
print("#" * 100)
p = Person("Vitalik")
print(type(p)) 
print(dir(p))
print(id(p))
print(p.__dict__)
help(p)

import inspect 

print(inspect.isclass(requests))  
print(inspect.isfunction(requests))
print(inspect.ismodule(math))
print(inspect.getsource(Person))
print("+" * 100)
def analyze (obj):
    print(f"Type: * {type(obj)}")
    print(f"Attributes: * {dir(obj)}"  )
    print(f"Documentation: * {obj.__doc__}")

analyze(add)
analyze(Person)
analyze(p)
    