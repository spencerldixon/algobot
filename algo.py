import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import forexconnect as fc
import settings

# Clients
fxcm            = fc.ForexConnectClient(
                    settings.FXCM_USERNAME,
                    settings.FXCM_PASSWORD,
                    settings.FXCM_ACCOUNT
                    )

# conn        = psql.connect(database=pg_database, user=pg_username, password=pg_password, host=pg_host, port=pg_port)

def get_chart(currency_pair):
    # Get the last days worth of tick data, fit to pandas dataframe, resample to size
    now         = datetime.now()
    then        = now - datetime.timedelta(days = 1)
    data        = client.get_historical_prices(currency_pair, then, now)
    attributes  = ['date', 'open', 'high', 'low', 'close']
    dataframe   = pd.DataFrame([[getattr(i, j) for j in attributes] for i in data], columns = attributes)

    print(dataframe.to_string())

    # Resample the chart to 2hr or whatever and trim the data
    # (the idea is that the beginning of the chart is the last timeframe (old MACD) the end is the latest timeframe (new MACD)
    # Get the MACD
    # Figure out if the MACD at the beginning is different to the MACD at the end of the timetrame




# def strategy(currency_pair, time_frame):
    # chart       = get_chart(currency_pair, time_frame)
    # snapshot    = get_chart_at(currency_pair, time_frame, )
    # get the chart data from FXCM
    # Drop the most recent bar (as it is still being formed and represents incomplete data)
    # If trade with currency pair and time frame exists in DB, then pull it out
        # Compare to see if macd has crossed
            # If it has, send an alert and update the record, waiting for it to cross back
            # update_snapshot(snapshot, )
            # send_alert("MACD has crossed on the {0} chart on {1}. You might want to check this out to see if it is a valid entry".format(time_frame, currency_pair))
        # Else update the last checked at timestamp and do nothing
    # Else if no trade exists, create it

# def apply_strategy_to_all_currencies(currencies, time_frame):
    # for currency in currencies:
        # strategy(currency, time_frame)

# Snapshots API

# def create_snapshot():

# def find_last_snapshot(currency_pair, time_frame):
    # cur = conn.cursor()

# Alerts
def send_alert(msg):
    # Post the message to endpoint or email or something or other
    print msg

if __name__ == '__main__':
    get_chart("GBP/USD")
    # from apscheduler.schedulers.blocking import BlockingScheduler
    # sched = BlockingScheduler(timezone='GMT')
    # sched.add_job(send_alert, 'interval', ["Every second!"],  seconds=1)
    # sched.add_job(send_alert, 'interval', ["Hello world!"],  seconds=5)
    # sched.start()

