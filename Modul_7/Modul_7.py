import requests
from bs4 import BeautifulSoup

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
dollars = soup.find('table', {'class':'mfd-table mfd-currency-table'})
dollars = dollars.find_all('td')
doll = ([dollar.text for dollar in dollars])
change = []
del doll[2::3]

print(doll)