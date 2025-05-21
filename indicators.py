import pandas as pd
import ta

def apply_indicators(df, settings):
    # RSI
    if settings.get('rsi', {}).get('enabled', False):
        periods = settings['rsi'].get('periods', [14])
        for period in periods:
            df[f'RSI_{period}'] = ta.momentum.RSIIndicator(df['close'], window=period).rsi()
    
    # MACD
    if settings.get('macd', {}).get('enabled', False):
        macd = ta.trend.MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()
    
    # Bollinger Bands
    if settings.get('bollinger', {}).get('enabled', False):
        window = settings['bollinger'].get('window', 20)
        window_dev = settings['bollinger'].get('window_dev', 2)
        bb = ta.volatility.BollingerBands(df['close'], window=window, window_dev=window_dev)
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()
    
    # Moving Averages (SMA)
    if settings.get('ma', {}).get('enabled', False):
        periods = settings['ma'].get('periods', [7, 14, 50, 200])
        for period in periods:
            df[f'SMA_{period}'] = ta.trend.SMAIndicator(df['close'], window=period).sma_indicator()
    
    # Exponential Moving Averages (EMA)
    if settings.get('ema', {}).get('enabled', False):
        periods = settings['ema'].get('periods', [7, 14, 50, 200])
        for period in periods:
            df[f'EMA_{period}'] = ta.trend.EMAIndicator(df['close'], window=period).ema_indicator()
    
    # Stochastic RSI
    if settings.get('stoch_rsi', {}).get('enabled', False):
        stoch = ta.momentum.StochRSIIndicator(df['close'])
        df['StochRSI_k'] = stoch.stochrsi_k()
        df['StochRSI_d'] = stoch.stochrsi_d()
    
    # Volume (Hacim)
    if settings.get('volume', {}).get('enabled', False):
        ma_period = settings['volume'].get('ma_period', 20)
        df['Volume_MA'] = df['volume'].rolling(window=ma_period).mean()
    
    # Parabolic SAR
    if settings.get('parabolic_sar', {}).get('enabled', False):
        sar = ta.trend.PSARIndicator(df['high'], df['low'], df['close'])
        df['Parabolic_SAR'] = sar.psar()
    
    # Ichimoku Cloud
    if settings.get('ichimoku', {}).get('enabled', False):
        ichimoku = ta.trend.IchimokuIndicator(df['high'], df['low'])
        df['Ichimoku_a'] = ichimoku.ichimoku_a()
        df['Ichimoku_b'] = ichimoku.ichimoku_b()
    
    # ATR
    if settings.get('atr', {}).get('enabled', False):
        atr = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close'])
        df['ATR'] = atr.average_true_range()

    # SuperTrend (manuel hesaplama)
    if settings.get('supertrend', {}).get('enabled', False):
        multiplier = settings['supertrend'].get('multiplier', 3)
        df['HL2'] = (df['high'] + df['low']) / 2
        atr_val = ta.volatility.AverageTrueRange(df['high'], df['low'], df['close']).average_true_range()
        df['Upper_Band'] = df['HL2'] + (multiplier * atr_val)
        df['Lower_Band'] = df['HL2'] - (multiplier * atr_val)

    return df
