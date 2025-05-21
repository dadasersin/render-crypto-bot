INDICATORS_CONFIG = {
    "RSI": {"enabled": True, "periods": [7, 14, 24]},
    "MACD": {"enabled": True, "fast": 12, "slow": 26, "signal": 9},
    "BollingerBands": {"enabled": True, "period": 20, "std_dev": 2},
    "MovingAverage": {"enabled": True, "periods": [7, 14, 50, 200]},
    "EMA": {"enabled": True, "periods": [7, 14, 50, 200]},
    "StochasticRSI": {"enabled": False},
    "Volume": {"enabled": True},
    "ParabolicSAR": {"enabled": False},
    "Ichimoku": {"enabled": False},
    "ATR": {"enabled": True, "period": 14}
}
