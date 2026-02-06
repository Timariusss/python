class Dog:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.energy = 50
        self.happiness = 50
        self.days = 0

    def status(self):
        print(f"День {self.days}")
        print(f"Голод: {self.hunger}")
        print(f"Энергия: {self.energy}")
        print(f"Настроение: {self.happiness}")
        print("-" * 30)

    def eat(self):
        self.hunger -= 10
        self.energy += 5
        print(f"{self.name} поел 🦴")

    def play(self):
        self.happiness += 10
        self.energy -= 10
        self.hunger += 10
        print(f"{self.name} поиграл 🎾")

    def sleep(self):
        self.energy += 20
        self.hunger += 5
        print(f"{self.name} поспал 😴")

    def new_day(self):
        self.days += 1
        print(f"\nДень {self.days}")

        if self.days % 5 != 0:
            self.play()
        else:
            self.happiness -= 20
            print(f"{self.name} не играл 😐")

        if self.days % 30 != 0:
            self.eat()
        else:
            self.hunger += 20
            print(f"{self.name} не ел 😣")

        if self.days % 10 != 0:
            self.sleep()
        else:
            self.energy -= 20
            print(f"{self.name} не спал 😴❌")

        self.hunger = max(0, min(100, self.hunger))
        self.energy = max(0, min(100, self.energy))
        self.happiness = max(0, min(100, self.happiness))

        self.status()


dog = Dog("Рексик")

print("🐶 Игра началась!\n")

while dog.days < 100:
    dog.new_day()

print("🎉 Игра завершена!")
print(f"Рексик прожил {dog.days} дней 🐾")

