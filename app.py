import streamlit as st
import yfinance as yf
from indicators import apply_indicators
from plot import plot_indicators
from config import settings

st.title("📈 Kripto İndikatör Dashboard")

symbol = st.text_input("Kripto Sembolü (örn. BTC-USD)", value="BTC-USD")

if st.button("Veriyi Getir ve Grafiği Göster"):
    df = yf.download(symbol, period="30d", interval="1d")
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)
        df = apply_indicators(df, settings)
        fig = plot_indicators(df, settings)
        st.pyplot(fig)
