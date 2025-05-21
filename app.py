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

# Sidebar'da indikatör aktif/pasif seçimi ve parametreleri
st.sidebar.header("İndikatör Ayarları")

for ind_name, ind_params in settings.items():
    with st.sidebar.expander(ind_name, expanded=False):
        enabled = st.checkbox(f"{ind_name} aktif mi?", value=ind_params.get('enabled', True))
        settings[ind_name]['enabled'] = enabled
        # Parametre varsa göster
        for key, val in ind_params.items():
            if key != 'enabled':
                if isinstance(val, list):
                    # Listeleri text input olarak alabiliriz (örneğin [7,14,24])
                    val_str = ','.join(map(str, val))
                    new_val = st.text_input(f"{ind_name} - {key}", val_str)
                    try:
                        new_list = list(map(int, new_val.split(',')))
                        settings[ind_name][key] = new_list
                    except:
                        pass
                elif isinstance(val, (int, float)):
                    new_val = st.number_input(f"{ind_name} - {key}", value=val)
                    settings[ind_name][key] = new_val
                else:
                    # Diğer tipleri olduğu gibi bırak
                    pass

if st.button("Veriyi Getir ve Grafiği Göster"):
    df = yf.download(symbol, period=period, interval=interval)
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)
        df = apply_indicators(df, settings)

        st.subheader("Fiyat Grafiği ve İndikatörler")
        plot_indicators(df, settings)

        st.subheader("İndikatör Veri Çıktıları (son 10 satır)")
        # Sadece aktif indikatörlerin sütunlarını seç
        active_cols = []
        for ind_name, ind_params in settings.items():
            if ind_params.get('enabled', False):
                for col in df.columns:
                    if ind_name.lower() in col.lower():
                        active_cols.append(col)
        active_cols = list(set(active_cols))
        st.dataframe(df[active_cols].tail(10))
