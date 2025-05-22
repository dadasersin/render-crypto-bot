from binance_api import place_order, get_balance

# İşlem başına kullanılacak USDT miktarı (dilediğin gibi ayarla)
trade_amount_usdt = 50  

def execute_trades(df, symbol='BTCUSDT'):
    position = False  # Pozisyonda olup olmadığını takip etmek için basit değişken
    for i, row in df.iterrows():
        signal = row.get('signal')  # Sinyal kolonunun adı 'signal' olmalı (buy, sell veya None)
        price = row.get('close')

        if signal == 'buy' and not position:
            quantity = trade_amount_usdt / price
            quantity = round(quantity, 6)  # Binance için genelde 6 basamak yeterli
            order = place_order(symbol, 'BUY', quantity)
            if order:
                position = True

        elif signal == 'sell' and position:
            quantity = trade_amount_usdt / price
            quantity = round(quantity, 6)
            order = place_order(symbol, 'SELL', quantity)
            if order:
                position = False
        else:
            # İşlem yok veya pozisyon durumuna göre bekleniyor
            pass

from binance_api import place_order, get_balance

trade_amount_usdt = 50  # İşlem başına kullanılacak USDT miktarı

def execute_trades(df, symbol='BTCUSDT'):
    position = False  # Pozisyonda olup olmadığını takip etmek için basit değişken

    for i, row in df.iterrows():
        signal = row.get('signal')  # 'buy', 'sell' veya None
        price = row.get('close')

        if signal == 'buy' and not position:
            quantity = trade_amount_usdt / price
            quantity = round(quantity, 6)  # Binance hassasiyeti

            order = place_order(symbol, 'BUY', quantity)
            if order and order.get('status') == 'FILLED':
                print(f"Alım emri verildi: {quantity} {symbol} @ {price}")
                position = True
            else:
                print(f"Alım emri başarısız: {order}")

        elif signal == 'sell' and position:
            quantity = trade_amount_usdt / price
            quantity = round(quantity, 6)

            order = place_order(symbol, 'SELL', quantity)
            if order and order.get('status') == 'FILLED':
                print(f"Satış emri verildi: {quantity} {symbol} @ {price}")
                position = False
            else:
                print(f"Satış emri başarısız: {order}")

        else:
            # İşlem yok veya pozisyon durumu ile uyumsuz sinyal
            pass
