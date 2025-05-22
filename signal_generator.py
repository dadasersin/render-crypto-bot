def generate_signals(df, settings):
    """
    Basit örnek sinyal üretme:
    - RSI 14 alt 30 ise BUY
    - RSI 14 üst 70 ise SELL
    - Diğer durumlarda NONE

    İstersen burayı istediğin gibi değiştirebilirsin.
    """

    signals = []
    rsi_period = 14
    rsi_col = f'RSI_{rsi_period}'
    
    for idx, row in df.iterrows():
        if rsi_col in df.columns:
            rsi = row[rsi_col]
            if rsi < 30:
                signals.append('buy')
            elif rsi > 70:
                signals.append('sell')
            else:
                signals.append('none')
        else:
            signals.append('none')
    
    df['signal'] = signals
    return df

