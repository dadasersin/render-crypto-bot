import ta

def apply_indicators(df, settings):
    # close sütununu 1D Series yap
    close_series = df['close']
    if hasattr(close_series, 'squeeze'):
        close_series = close_series.squeeze()
    
    if settings.get('rsi', {}).get('enabled', False):
        for period in settings['rsi'].get('periods', [14]):
            df[f'RSI_{period}'] = ta.momentum.RSIIndicator(close_series, window=period).rsi()

    if settings.get('macd', {}).get('enabled', False):
        macd = ta.trend.MACD(close_series)
        df['MACD'] = macd.macd()
        df['MACD_signal'] = macd.macd_signal()

    if settings.get('bollinger', {}).get('enabled', False):
        bb = ta.volatility.BollingerBands(close_series)
        df['BB_upper'] = bb.bollinger_hband()
        df['BB_lower'] = bb.bollinger_lband()

    # Diğer indikatörler burada aynı mantıkla aktifse hesaplanır...

    return df
