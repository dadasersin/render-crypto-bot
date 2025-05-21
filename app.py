import streamlit as st
import yfinance as yf
from indicators import apply_indicators
from plot import plot_indicators
from config import settings

st.set_page_config(page_title="Kripto İndikatör Dashboard", layout="wide")

st.title("📈 Kripto İndikatör Dashboard")

symbol = st.text_input("Kripto Sembolü (örn. BTC-USD)", value="BTC-USD")
period = st.selectbox("Veri Periyodu", options=["30d", "60d", "90d", "180d", "365d"], index=3)
interval = st.selectbox("Aralık", options=["1d", "1h", "30m"], index=0)

if st.button("Veriyi Getir ve Grafiği Göster"):
    df = yf.download(symbol, period=period, interval=interval)
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)
        df = apply_indicators(df, settings)
        st.subheader("Fiyat Grafiği ve İndikatörler")
        fig = plot_indicators(df, settings)  # plot_indicators fig döndürmeli
        st.pyplot(fig)
