import requests
import time

THREECOMMAS_API_KEY = 'API_KEYINIZ'
THREECOMMAS_API_SECRET = 'API_SECRETINIZ'
THREECOMMAS_ACCOUNT_ID = 'HESAP_ID'

RENDER_SIGNAL_API = 'https://render-crypto-bot-1.onrender.com/signal'

def get_latest_signal():
    response = requests.get(RENDER_SIGNAL_API)
    if response.status_code == 200:
        data = response.json()
        return data['signal'], data['price']
    else:
        return None, None

def place_3commas_order(signal, price):
    # 3Commas API için uygun istek yap
    # Bu örnek sadece konsept içindir, gerçek API kullanımı için imzalama ve endpointleri kontrol et
    print(f"Signal: {signal} Price: {price}")
    if signal == 'buy':
        print("3Commas: Buy order place!")
        # API çağrısı yapılacak
    elif signal == 'sell':
        print("3Commas: Sell order place!")
        # API çağrısı yapılacak
    else:
        print("No action.")

if __name__ == "__main__":
    while True:
        signal, price = get_latest_signal()
        if signal:
            place_3commas_order(signal, price)
        time.sleep(60)  # 1 dakikada bir kontrol et

