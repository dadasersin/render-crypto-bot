import streamlit as st
import yfinance as yf
import pandas as pd
from indicators import apply_indicators
from plot import plot_indicators
from config import settings

st.set_page_config(page_title="Kripto İndikatör Dashboard", layout="wide")

st.title("📈 Kripto İndikatör Dashboard")

# Kullanıcıdan sembol, tarih ve aralık seçimi
symbol = st.text_input("Kripto Sembolü (örn. BTC-USD)", value="BTC-USD")
period = st.selectbox("Veri Periyodu", options=["30d", "60d", "90d", "180d", "365d"], index=3)
interval = st.selectbox("Aralık", options=["1d", "1h", "30m"], index=0)

# İndikatör ayarlarını config'den okuyup göster (basitçe)
st.sidebar.header("İndikatör Ayarları")
for ind_name, ind_params in settings.items():
    with st.sidebar.expander(ind_name):
        for param, val in ind_params.items():
            new_val = st.number_input(f"{param}", value=val)
            settings[ind_name][param] = new_val

if st.button("Veriyi Getir ve Grafiği Göster"):

    with st.spinner(f"{symbol} verisi indiriliyor..."):
        df = yf.download(symbol, period=period, interval=interval)
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)

        with st.spinner("İndikatörler hesaplanıyor..."):
            df = apply_indicators(df, settings)

        st.subheader("Fiyat Grafiği ve İndikatörler")
        plot = plot_indicators(df, settings)
        st.pyplot(plot)

        # Aktif indikatörlerin ham verilerini göster
        st.subheader("İndikatör Veri Çıktıları (son 10 satır)")
        active_cols = [col for col in df.columns if any(ind in col for ind in settings.keys())]
        st.dataframe(df[active_cols].tail(10))


