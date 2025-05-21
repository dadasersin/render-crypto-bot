import matplotlib.pyplot as plt

def plot_indicators(df, settings):
    fig, ax = plt.subplots(figsize=(15, 10))
    ax.plot(df['close'], label='Close Price', color='black')

    if settings.get('rsi', {}).get('enabled', False):
        for period in settings['rsi'].get('periods', []):
            rsi_col = f'RSI_{period}'
            if rsi_col in df:
                ax.plot(df[rsi_col], label=f'RSI {period}')

    if settings.get('macd', {}).get('enabled', False):
        if 'MACD' in df and 'MACD_signal' in df:
            ax.plot(df['MACD'], label='MACD')
            ax.plot(df['MACD_signal'], label='MACD Signal')

    if settings.get('bollinger', {}).get('enabled', False):
        if 'BB_upper' in df and 'BB_lower' in df:
            ax.plot(df['BB_upper'], label='BB Upper')
            ax.plot(df['BB_lower'], label='BB Lower')

    # Diğer indikatörler için de benzer şekilde çizim yap...

    ax.legend()
    ax.set_title('Teknik İndikatörler Grafiği')
    return fig
