from flask import Flask, jsonify

app = Flask(__name__)

# Burada sinyal dinamik olarak hesaplanabilir, şimdilik sabit örnek
current_signal = "buy"  # "buy", "sell", veya None

@app.route("/signal")
def signal():
    return jsonify({"signal": current_signal})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)

