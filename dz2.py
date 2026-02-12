
class Engine:
    def __init__(self, power):
        self.power = power  

    def start_engine(self):
        print(f"Двигатель мощностью {self.power} л.с. запущен")



class Wheels:
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count 

    def rotate_wheels(self):
        print(f"Колеса ({self.wheel_count} шт.) вращаются")



class Car(Engine, Wheels):
    def __init__(self, power, wheel_count, brand):
        Engine.__init__(self, power)
        Wheels.__init__(self, wheel_count)
        self.brand = brand  

    def info(self):
        print(f"Марка машины: {self.brand}")



car1 = Car(150, 4, "BMW")

car1.info()
car1.start_engine()
car1.rotate_wheels()
