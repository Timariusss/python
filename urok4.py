
class Human:    
    height = 162


class Student(Human):
    satiety = 2


class Worker(Human):
    satiety = 100 

nick = Student()
olya = Worker()
print(nick.height)
print(olya.height)
print(nick.satiety)
print(olya.satiety)

class Grandfather:
    height = 170 
    satiety = 100 
    age = 60 

class Parent(Grandfather):
    age = 40 

class Child(Parent): 
    age = 20 
    satiety = 50  
    height = 182 
    def __init__(self):
        print(self.height)
        print(self.satiety)
        print(self.age)

nick = Child()

class Grandfather:
    def about(self):
        print("I am grandmother")

    def about_myself(self):
        print("I am grandfather")


class Parent(Grandfather):
    def about(self):
        print("I am parent")


class Child(Parent): 
  
 def __init__(self):
   super().about()
   super().about_myself()

nick = Child()