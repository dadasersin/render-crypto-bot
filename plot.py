import matplotlib.pyplot as plt

def plot_indicators(df, settings):
    fig, ax = plt.subplots(figsize=(15, 10))
    
    ax.plot(df['close'], label='Close Price', color='black')

    # Örnek RSI çizimi
    if settings.get('rsi', {}).get('enabled', False):
        for period in settings['rsi'].get('periods', []):
            rsi_col = f'RSI_{period}'
            if rsi_col in df:
                ax.plot(df[rsi_col], label=f'RSI {period}')
    
    ax.legend()
    ax.set_title('Teknik İndikatörler Grafiği')
    return fig
