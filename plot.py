import matplotlib.pyplot as plt

def plot_indicators(df, settings):
    plt.figure(figsize=(15, 10))
    
    plt.plot(df['close'], label='Close Price', color='black')

    # RSI
    for period in settings.get('rsi', []):
        rsi_col = f'RSI_{period}'
        if rsi_col in df:
            plt.plot(df[rsi_col], label=f'RSI {period}')

    # MACD
    if settings.get('macd', False):
        if 'MACD' in df and 'MACD_signal' in df:
            plt.plot(df['MACD'], label='MACD')
            plt.plot(df['MACD_signal'], label='MACD Signal')

    # Bollinger Bands
    if settings.get('bollinger', False):
        if 'BB_upper' in df and 'BB_lower' in df:
            plt.plot(df['BB_upper'], label='BB Upper')
            plt.plot(df['BB_lower'], label='BB Lower')

    # SMA
    for period in settings.get('ma', []):
        sma_col = f'SMA_{period}'
        if sma_col in df:
            plt.plot(df[sma_col], label=f'SMA {period}')

    # EMA
    for period in settings.get('ema', []):
        ema_col = f'EMA_{period}'
        if ema_col in df:
            plt.plot(df[ema_col], label=f'EMA {period}')

    # Stochastic RSI
    if settings.get('stoch_rsi', False):
        if 'StochRSI_k' in df and 'StochRSI_d' in df:
            plt.plot(df['StochRSI_k'], label='Stoch RSI %K')
            plt.plot(df['StochRSI_d'], label='Stoch RSI %D')

    # Parabolic SAR
    if settings.get('parabolic_sar', False):
        if 'Parabolic_SAR' in df:
            plt.scatter(df.index, df['Parabolic_SAR'], label='Parabolic SAR', color='purple', marker='.')

    # Ichimoku Cloud
    if settings.get('ichimoku', False):
        if 'Ichimoku_a' in df and 'Ichimoku_b' in df:
            plt.plot(df['Ichimoku_a'], label='Ichimoku A')
            plt.plot(df['Ichimoku_b'], label='Ichimoku B')

    # ATR
    if settings.get('atr', False):
        if 'ATR' in df:
            plt.plot(df['ATR'], label='ATR')

    # SuperTrend Bands
    if settings.get('supertrend', False):
        if 'Upper_Band' in df and 'Lower_Band' in df:
            plt.plot(df['Upper_Band'], label='SuperTrend Upper Band', linestyle='--')
            plt.plot(df['Lower_Band'], label='SuperTrend Lower Band', linestyle='--')

    plt.legend()
    plt.title('Teknik İndikatörler Grafiği')
    plt.show()

