# Algobot

Algobot is a Python trading bot that using the FXCM ForexConnect API.

## How does it work?

Algobot repeatedly monitors the charts at set timeframes looking for MACD crossovers. When it finds a suitable crossover, it will watch the trade looking for confirmation and significant movement. If the potential trade is confirmed, Algobot will send you a notification so that you can review it and place the trade if it meets your criteria. If not, then Algobot drops the watched traded and keeps looking.

## Installation

1. Spin up a Ubuntu box on Digital Ocean (you will need at least 1GB of RAM to build the necessary libraries, although you can scale this down once installed)
2. Install Boost 1.54 (Follow the third comment here: https://stackoverflow.com/questions/12578499/how-to-install-boost-on-ubuntu)
3. Follow installation instructions for the python-forexconnect API (https://github.com/neka-nat/python-forexconnect)
4. Install PostgreSQL
5. Configure Algobot in `config.py`

## Configuration

You can specify which currency pairs and chart timeframes you want Algobot to watch in `config.py`

## Run it

Just run the file and let it go

`python algo.py`

## Trade Alerts

You can receive alerts whenever Algobot spots a potential juicy trade. This can be done by sending a JSON payload to a custom endpoint (this lands nicely in my AI personal assistant which is then sent via a notification to me)


## When it fucks up on Digital Ocean...

For some reason the API breaks whenever the server is restarted, to fix this, run...

```
export FOREXCONNECT_ROOT=~/ForexConnectAPI-1.4.1-Linux-x86_64 && export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:~/ForexConnectAPI-1.4.1-Linux-x86_64/lib && cd python-forexconnect/build/ && cmake .. -DDEFAULT_FOREX_URL="http://www.fxcorporate.com/Hosts.jsp" && make install
```
