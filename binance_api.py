from binance.client import Client
import os

# Ortam değişkenlerinden API anahtarlarını alıyoruz
API_KEY = os.getenv('BINANCE_API_KEY')
API_SECRET = os.getenv('BINANCE_API_SECRET')

client = Client(API_KEY, API_SECRET)

def get_balance(asset='USDT'):
    balance = client.get_asset_balance(asset)
    return float(balance['free']) if balance else 0.0

def place_order(symbol, side, quantity):
    try:
        order = client.create_order(
            symbol=symbol,
            side=side,
            type='MARKET',
            quantity=quantity
        )
        print(f"Order placed: {order}")
        return order
    except Exception as e:
        print(f"Order error: {e}")
        return None

def get_current_price(symbol):
    ticker = client.get_symbol_ticker(symbol=symbol)
    return float(ticker['price'])

