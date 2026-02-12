class Client:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"{self.name} пополнил счет на {amount}. Баланс: {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"{self.name} снял {amount}. Баланс: {self.balance}")
        else:
            print(f"{self.name} недостаточно средств!")



class Bank:
    def __init__(self, name):
        self.name = name
        self.clients = []

    def add_client(self, client):
        self.clients.append(client)
        print(f"Клиент {client.name} добавлен в банк {self.name}")

    def show_clients(self):
        print(f"\nКлиенты банка {self.name}:")
        for client in self.clients:
            print(f"{client.name} — Баланс: {client.balance}")



bank = Bank("PrivatBank")

client1 = Client("Tymur", 1000)
client2 = Client("Anna", 500)

bank.add_client(client1)
bank.add_client(client2)

client1.deposit(300)
client2.withdraw(200)

bank.show_clients()
