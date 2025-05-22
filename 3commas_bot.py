import requests
import time

THREECOMMAS_API_KEY = 'a245da1dad234401a48c488ace17aa87daadbd4ec9ad4cdf839cd002328c9ca0'
THREECOMMAS_API_SECRET = 'b9560ea635dfefef9c43fa4ccf9184caf1d66933959acabbc7f43c213b728248085986efae632d78fa20a671e2bd91bea944a82e5f76b1a3e07418ffd74ff725aa8f6e3f045c11d6ce28927eedffdc81e02440616ffe8f5611f17d90f219b0942a165040
'
THREECOMMAS_ACCOUNT_ID = '1038893'

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

