import requests
from bs4 import BeautifulSoup
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator


page = requests.get('http://mfd.ru/currency/?currency=USD')
soup = BeautifulSoup(page.text, 'html.parser')
dollars = soup.find('table', {'class':'mfd-table mfd-currency-table'})
dollars = dollars.find_all('td')

doll = ([dollar.text for dollar in dollars][-2:2:-3])
doll = [float(x) for x in doll]
dates = ([dollar.text[2:] for dollar in dollars][-3:2:-3])

print(doll)
print(dates)

fig, ax = plt.subplots()

ax.xaxis.set_major_locator(MaxNLocator(12))
ax.grid()

ax.set_title('Курс доллара', fontname="fantasy", fontsize=20)
ax.set_xlabel('Дата', fontsize=15, color='g')
ax.set_ylabel('USD', fontsize=15, color='g')
ax.plot(dates, doll, color= 'g')

plt.show()