# Takes in a csv of data for each currency pair
# Adjusts to timeframes and runs your strategy against it alongside a random pick (buy/sell)
# Outputs the results to see how well your strategy performed

account_size    = 2000
risk            = 1
time_frames     = ["1d", "8hr", "2hr"]


# Outputs:

# total months/days traded
# total % gain/loss
# total $ gain/loss
# average hit rate
# average run in pips
# average monthly % gain
# frequency (trades made per month)

# prints a table for figures for each week/month
