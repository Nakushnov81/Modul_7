import requests
from bs4 import BeautifulSoup

page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
dollars = soup.find_all('td' in 'tr', {'class':'mfd-table mfd-currency-table'})
print([dollar.text for dollar in dollars])