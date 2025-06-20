import ta

def evaluate_strategy(df, indicators):
    df['ema'] = ta.trend.EMAIndicator(df['close'], window=indicators['ema']).ema_indicator()
    # SMMA Approximation: zweifache Glättung
    df['smma'] = df['close'].ewm(span=indicators['smma'], adjust=False).mean().ewm(span=10).mean()

    c1 = df.iloc[-2]
    c2 = df.iloc[-1]

    # Candle Pattern
    bull_engulf = c2['close'] > c2['open'] and c2['open'] < c1['close'] and c2['close'] > c1['open']
    bear_engulf = c2['close'] < c2['open'] and c2['open'] > c1['close'] and c2['close'] < c1['open']

    # Trend & Pullback
    trend_up = c2['close'] > c2['smma']
    near_ema = abs(c2['close'] - c2['ema']) / c2['close'] < 0.005

    if trend_up and near_ema and bull_engulf:
        return "LONG"
    elif not trend_up and near_ema and bear_engulf:
        return "SHORT"
    return None
