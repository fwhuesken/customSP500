from bs4 import BeautifulSoup
from requests import get


url = 'https://finance.yahoo.com/quote/AAPL/key-statistics?p=AAPL'
response = get(url)
soup = BeautifulSoup(response.text, 'html.parser')

stock_data = soup.find_all("table")

for stock in stock_data:
    print(stock.text)

