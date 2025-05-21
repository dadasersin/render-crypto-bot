def apply_indicators(df, settings):
    # RSI
    if settings['rsi']['enabled']:
        for period in settings['rsi']['periods']:
            df[f'RSI_{period}'] = ta.momentum.RSIIndicator(df['close'], window=period).rsi()

    if settings['macd']['enabled']:
        macd = ta.trend.MACD(df['close'])
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()

    if settings['bollinger']['enabled']:
        window = settings['bollinger'].get('window', 20)
        window_dev = settings['bollinger'].get('window_dev', 2)
        bb = ta.volatility.BollingerBands(df['close'], window=window, window_dev=window_dev)
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()

    # ve diğer indikatörler de benzer şekilde...

    return df
