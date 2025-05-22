import streamlit as st
import yfinance as yf
from indicators import apply_indicators
from plot import plot_indicators
from config import settings

# Binance işlemleri için yeni modüller
from trading import execute_trades
from signals import generate_signals  # Sinyal oluşturma fonksiyonunu ayrıca tanımlamalısın

st.title("📈 Kripto İndikatör Dashboard")

symbol = st.text_input("Kripto Sembolü (örn. BTC-USD)", value="BTC-USD")

if st.button("Veriyi Getir ve Grafiği Göster"):
    df = yf.download(symbol, period="30d", interval="1d")
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)
        df = apply_indicators(df, settings)

        # Sinyalleri hesapla
        df = generate_signals(df)

        fig = plot_indicators(df, settings)
        st.pyplot(fig)

        # Eğer sinyal kolonu yoksa kullanıcıyı uyar
        if 'signal' not in df.columns:
            st.warning("Sinyal kolonunu oluşturmadınız, al-sat işlemi yapılmaz.")
        else:
            if st.button("Botu Çalıştır ve Al-Sat İşlemleri Yap"):
                execute_trades(df, symbol.replace('-', '').upper())
                st.success("Bot işlemi tamamlandı.")
