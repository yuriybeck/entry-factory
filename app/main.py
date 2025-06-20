import time
from data_fetcher import get_price_data
from strategy_engine import evaluate_strategy
from alert_system import send_alert
import yaml

with open("config.yaml") as f:
    config = yaml.safe_load(f)

while True:
    for symbol in config["symbols"]:
        for tf in config["timeframes"]:
            df = get_price_data(symbol, tf)
            signal = evaluate_strategy(df, config["indicators"])
            if signal:
                send_alert(config["telegram"], symbol, tf, signal)
    time.sleep(300)
