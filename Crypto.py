import requests
from bs4 import BeautifulSoup
import ccxt

def get_dominance():
    url = "https://www.tradingview.com/markets/cryptocurrencies/dominance/"

    response = requests.get(url)

    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        last_value_span = soup.find("div", class_="blockContent-GgmpMpKr")
        return last_value_span.text
    else:
        print("Ошибка при получении страницы:", response.status_code)

def get_cost_coins():
    exchange = ccxt.bybit()

    price_coins = []

    price_coins.append(exchange.fetch_ticker('BTC/USDT')['last'])
    price_coins.append(exchange.fetch_ticker('TON/USDT')['last'])
    price_coins.append(exchange.fetch_ticker('TNSR/USDT')['last'])

    return price_coins

# print(get_cost_coins())
