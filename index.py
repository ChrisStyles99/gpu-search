import requests
from bs4 import BeautifulSoup

URL = 'https://www.cyberpuerta.mx/Tarjetas-de-Video-Radeon-Serie-RX-5600-XT/'

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')

productCards = soup.find_all(class_="emproduct_right")
prices = soup.find_all(class_="price")
titles = []
cleanedPrices = []
titleAndPrice = []

for price in prices:
  price = price.get_text()
  cleanedPrices.append(price)

for x in range(len(productCards)):
  title = soup.find(id=f"productList-{x + 1}").get_text()
  titles.append(title)

for i in range(len(productCards)):
  print(titles[i], cleanedPrices[i])