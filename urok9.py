import requests 
from bs4 import BeautifulSoup

url = "https://uk.wikipedia.org/wiki/%D0%9A%D0%B8%D1%97%D0%B2"

headers = {'User-Agent': 'Mozilla/5.0'}

response = requests.get(url, headers=headers)
print(response.status_code)
soup = BeautifulSoup(response.text, "html.parser")
title = soup.find("h1").text 
print("название статьи:", title)

paragraph = soup.find("p").text
print(paragraph)

section = soup.find_all('h2')

for s in section:
    print(s.text)

links = soup.find_all("a")

print("количество ссылок: ", len(links))