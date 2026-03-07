import requests
import sqlite3


# ----- База данных -----
class DB:

    def __init__(self):
        self.conn = sqlite3.connect("rates.db")
        self.cur = self.conn.cursor()

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS rates(
        currency TEXT,
        rate REAL
        )
        """)
        self.conn.commit()

    def add(self, currency, rate):
        self.cur.execute("INSERT INTO rates VALUES (?, ?)", (currency, rate))
        self.conn.commit()

    def show(self):
        self.cur.execute("SELECT * FROM rates")
        rows = self.cur.fetchall()

        for row in rows:
            print(row)


# ----- Парсер -----
class Parser:

    def get_rate(self, currency):

        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        data = requests.get(url).json()

        for item in data:
            if item["cc"] == currency.upper():
                return item["rate"]

        return None


# ----- Интерфейс -----
class App:

    def __init__(self):
        self.db = DB()
        self.parser = Parser()

    def run(self):

        while True:

            currency = input("Введите валюту (USD, EUR) или exit: ")

            if currency.lower() == "exit":
                break

            rate = self.parser.get_rate(currency)

            if rate:
                print("Курс:", rate)
                self.db.add(currency, rate)
                print("Сохранено в базу")
            else:
                print("Валюта не найдена")

        print("\nВсе записи в базе:")
        self.db.show()


# запуск программы
if __name__ == "__main__":
    app = App()
    app.run()