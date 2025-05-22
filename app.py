import streamlit as st
import yfinance as yf
from indicators import apply_indicators
from plot import plot_indicators
from config import settings
from signal_generator import generate_signals
from flask import Flask, jsonify

st.title("📈 Kripto İndikatör Dashboard")

symbol = st.text_input("Kripto Sembolü (örn. BTC-USD)", value="BTC-USD")

if st.button("Veriyi Getir ve Grafiği Göster"):
    df = yf.download(symbol, period="30d", interval="1d")
    if df.empty:
        st.error("Veri bulunamadı.")
    else:
        df.rename(columns=str.lower, inplace=True)
        df = apply_indicators(df, settings)
        df = generate_signals(df, settings)
        fig = plot_indicators(df, settings)
        st.pyplot(fig)

        st.subheader("Son Sinyaller")
        st.dataframe(df[['close', 'signal']].tail(10))

# Flask uygulaması olarak API endpoint açmak için:
app = Flask(__name__)

@app.route('/signal')
def get_signal():
    df = yf.download(symbol, period="30d", interval="1d")
    if df.empty:
        return jsonify({"error": "Data not found"}), 404
    df.rename(columns=str.lower, inplace=True)
    df = apply_indicators(df, settings)
    df = generate_signals(df, settings)

    # En son sinyali JSON olarak gönder
    last_signal = df['signal'].iloc[-1]
    last_price = df['close'].iloc[-1]
    return jsonify({"symbol": symbol, "signal": last_signal, "price": last_price})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
