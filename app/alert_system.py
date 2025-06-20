import requests

def send_alert(telegram_config, symbol, timeframe, signal):
    msg = f"📢 {signal} SIGNAL – {symbol} – TF: {timeframe}"
    url = f"https://api.telegram.org/bot{telegram_config['token']}/sendMessage"
    data = {"chat_id": telegram_config["chat_id"], "text": msg}
    requests.post(url, data=data)
