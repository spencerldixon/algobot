import numpy as np
import talib as ta
import time
from apscheduler.scheduler import Scheduler
import forexconnect as fc
import psycopg2 as psql

fxcm        = fc.ForexConnectClient("username", "pass", "Real")
conn        = psql.connect(database="algodb", user="postgres", password="pass123", host="127.0.0.1", port="5432")
currencies  = ["GBP/USD", "NZD/CAD"]

def get_chart(currency_pair, time_frame):
    # Get the chart data for the particular time frame

def strategy(currency_pair, time_frame):
    chart       = get_chart(currency_pair, time_frame)
    snapshot    = find_last_snapshot(currency_pair, time_frame)
    # get the chart data from FXCM
    # If trade with currency pair and time frame exists in DB, then pull it out
        # Compare to see if macd has crossed
            # If it has, send an alert and update the record, waiting for it to cross back
            update_snapshot(snapshot, )
            send_alert("MACD has crossed on the {0} chart on {1}. You might want to check this out to see if it is a valid entry".format(time_frame, currency_pair))
        # Else update the last checked at timestamp and do nothing
    # Else if no trade exists, create it

def apply_strategy_to_all_currencies(currencies, time_frame):
    for currency in currencies:
        strategy(currency, time_frame)

# Snapshots API

def create_snapshot():
    cur = conn.cursor()
    cur.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
            VALUES (1, 'Paul', 32, 'California', 20000.00)");
    conn.commit()

def find_last_snapshot(currency_pair, time_frame):
    cur = conn.cursor()

# Alerts

def send_alert(message):
    # Post the message to endpoint or email or something or other

# Schedule when to run strategy and run it
scheduler = BlockingScheduler()
scheduler.add_job(apply_strategy_to_all_currencies(currencies, "1d")), 'cron', day_of_week='mon-fri', hour=8)
scheduler.add_job(apply_strategy_to_all_currencies(currencies, "8hr")), 'interval', hours=8)
scheduler.add_job(apply_strategy_to_all_currencies(currencies, "2hr")), 'interval', hours=2)
scheduler.start()
