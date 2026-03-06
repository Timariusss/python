import requests
import sqlite3
from bs4 import BeautifulSoup
from datetime import datetime

conn = sqlite3.connect("weather.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS weather (
    date TEXT,
    time TEXT,
    temperature TEXT
)
""")

url = "https://sinoptik.ua/погода-днепр"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")

# ищем температуру
temp_tag = soup.find("p", class_="today-temp")

if temp_tag:
    temperature = temp_tag.text.strip()
else:
    temperature = "Невідомо"

now = datetime.now()
date = now.strftime("%Y-%m-%d")
time = now.strftime("%H:%M:%S")

cursor.execute(
    "INSERT INTO weather (date, time, temperature) VALUES (?, ?, ?)",
    (date, time, temperature)
)

conn.commit()

print("Температура:", temperature)
print("Дані записані у базу!")

conn.close()