import requests


class CurrencyConverter:
    def __init__(self):
        self.usd_rate = self.get_usd_rate()

    def get_usd_rate(self):
        url = "https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?json"
        response = requests.get(url)
        data = response.json()

        for currency in data:
            if currency["cc"] == "USD":
                return currency["rate"]

    def convert_to_usd(self, uah):
        return uah / self.usd_rate


converter = CurrencyConverter()

uah = float(input("Введіть суму в гривнях: "))

usd = converter.convert_to_usd(uah)

print(f"{uah} грн = {usd:.2f} USD")