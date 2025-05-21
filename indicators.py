import ta

def apply_indicators(df, settings):
    if settings.get('rsi', {}).get('enabled', False):
        for period in settings['rsi'].get('periods', [14]):
            df[f'RSI_{period}'] = ta.momentum.RSIIndicator(df['close'], window=period).rsi()

    if settings.get('macd', {}).get('enabled', False):
        macd = ta.trend.MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()

    if settings.get('bollinger', {}).get('enabled', False):
        bb = ta.volatility.BollingerBands(df['close'])
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()

    # Diğer indikatörler burada aynı mantıkla aktifse hesaplanır...

    return df
