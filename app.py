import streamlit as st
import yfinance as yf
import datetime
import pandas as pd
import matplotlib.pyplot as plt
from collectData import dataScraper

st.set_page_config(page_title="QuantQuips", page_icon="chart_with_upwards_trend", layout='wide')

st.title("QuantQuips")
st.write("Welcome to the home page of QuantQuips Description to go here.")

ind1,ind2,ind3,ind4 = st.columns(4)
CONTAINER_HEIGHT = 500

index_ticker = ["^NSEI","^BSESN","^NDX","^GSPC"]

def current_price(instrument):
    data = yf.Ticker(instrument).history(period="1d", interval="30m")
    return data["Close"]

with ind1:
        with st.container(border=True):
                nse_ticker_val = current_price(index_ticker[0])
                nse_ticker_curr = str(nse_ticker_val.iloc[-1])
                st.metric(label="Nifty 50",value=nse_ticker_curr[0:11],delta=nse_ticker_val.pct_change().iloc[-1])
with ind2:
        with st.container(border=True):
                bse_tick_val = current_price(index_ticker[1])
                bse_ticker_curr = str(bse_tick_val.iloc[-1])
                st.metric(label="Sensex 60",value=bse_ticker_curr[0:11],delta=bse_tick_val.pct_change().iloc[-1])
with ind3:
        with st.container(border=True):
                ndx_tick_val = current_price(index_ticker[2])
                ndx_ticker_curr = str(ndx_tick_val.iloc[-1])
                st.metric(label="Nasdaq 100",value=ndx_ticker_curr[0:11],delta=ndx_tick_val.pct_change().iloc[-1])
with ind4:
        with st.container(border=True):
                gspc_tick_val = current_price(index_ticker[3])
                gspc_ticker_curr = str(gspc_tick_val.iloc[-1])
                st.metric(label="S&P 500",value=gspc_ticker_curr[0:11],delta=gspc_tick_val.pct_change().iloc[-1])
                