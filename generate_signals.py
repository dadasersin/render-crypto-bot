def generate_signals(df):
    df['signal'] = None
    # Örnek: RSI 14 30 altı al, 70 üstü sat
    if 'RSI_14' in df.columns:
        df.loc[df['RSI_14'] < 30, 'signal'] = 'buy'
        df.loc[df['RSI_14'] > 70, 'signal'] = 'sell'
    return df

