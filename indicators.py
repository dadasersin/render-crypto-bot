import pandas as pd
import ta

def apply_indicators(df, settings):
    # RSI
    for period in settings.get('rsi', [14]):
        df[f'RSI_{period}'] = ta.momentum.RSIIndicator(df['close'], window=period).rsi()
    
    # MACD
    if settings.get('macd', True):
        macd = ta.trend.MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()
    
    # Bollinger Bands
    if settings.get('bollinger', True):
        bb = ta.volatility.BollingerBands(df['close'], window=20, window_dev=2)
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()
    
    # Moving Averages (SMA)
    for period in settings.get('ma', [7, 14, 50, 200]):
        df[f'SMA_{period}'] = ta.trend.SMAIndicator(df['close'], window=period).sma_indicator()
    
    # Exponential Moving Averages (EMA)
    for period in settings.get('ema', [7, 14, 50, 200]):
        df[f'EMA_{period}'] = ta.trend.EMAIndicator(df['close'], window=period).ema_indicator()
    
    # Stochastic RSI
    if settings.get('stoch_rsi', True):
        stoch = ta.momentum.StochRSIIndicator(df['close'])
        df['StochRSI_k'] = stoch.stochrsi_k()
        df['StochRSI_d'] = stoch.stochrsi_d()
    
    # Volume (hacim)
    if settings.get('volume', True):
        df['Volume_MA_20'] = df['volume'].rolling(window=20).mean()
    
    # Parabolic SAR
    if settings.get('parabolic_sar', True):
        sar = ta.trend.PSARIndicator(df['high'], df['low'], df['close'])
        df['Parabolic_SAR'] = sar.psar()
    
    # Ichimoku Cloud
    if settings.get('ichimoku', True):
        ichimoku = ta.trend.IchimokuIndicator(df['high'], df['low'])
        df['Ichimoku_a'] = ichimoku.ichimoku_a()
        df['Ichimoku_b'] = ichimoku.ichimoku_b()
    
    # ATR
    if settings.get('atr', True):
        atr = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close'])
        df['ATR'] = atr.average_true_range()

    # SuperTrend (manuel hesaplama)
    if settings.get('supertrend', True):
        df['HL2'] = (df['high'] + df['low']) / 2
        atr = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close']).average_true_range()
        multiplier = settings.get('supertrend_multiplier', 3)
        df['Upper_Band'] = df['HL2'] + (multiplier * atr)
        df['Lower_Band'] = df['HL2'] - (multiplier * atr)

    return df
