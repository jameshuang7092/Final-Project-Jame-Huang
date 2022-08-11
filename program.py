import requests
from getpass import getpass
from pandas import read_csv
from numpy.ma.core import var # https://stackoverflow.com/questions/9390126/pythonic-way-to-check-if-something-exists
import plotly.graph_objects as go
import pandas as pd
#!pip install chart_studio
import chart_studio
import chart_studio.plotly as py
import chart_studio.presentation_objs as pres

try:
    symbol = input("Please input crypto ticker: ").upper()
    api_key = input("Enter API key for Alphavantage: ") #for some reason, getpass() is not working...
    market = input("Please input market outside the USA: ").upper()
    csv_url = f"https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=USD&apikey={api_key}&datatype=csv"

    df_local_upload = pd.read_csv (r'C:\Users\jamee\OneDrive\Desktop\plotly_final_1.csv')
    df_alphavantage = pd.read_csv(f'https://www.alphavantage.co/query?function=DIGITAL_CURRENCY_DAILY&symbol={symbol}&market=USD&apikey={api_key}&datatype=csv')
    var = df_alphavantage.timestamp[0]
    if var:
        print("This is a valid symbol.")

    fig = go.Figure([go.Scatter(x=df_alphavantage['timestamp'], y=df_alphavantage['close (USD)'])])
    fig.update_layout(title='Daily Crypto Prices in USA',
                       xaxis_title='Month',
                       yaxis_title=f'{symbol}')
    fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.2f')
    fig.show()
    df_uploaded = pd.DataFrame(list(df_local_upload.items()), columns = ['timestamp','BTC price in SK'])
    df_uploaded_csv = pd.read_csv(r'C:\Users\jamee\OneDrive\Desktop\plotly_final_1.csv')
    fig = go.Figure([go.Scatter(x=df_uploaded_csv['Date'], y=df_uploaded_csv['BTC price in SK'])])
    fig.update_layout(title='Daily Crypto Prices in non-US market',
                       xaxis_title='Month',
                       yaxis_title=f'{symbol}')
    fig.update_layout(yaxis_tickprefix = '$', yaxis_tickformat = ',.2f')
    fig.show()
    trace0 = go.Scatter(
        x=df_uploaded_csv['Date'],
        y=df_uploaded_csv['close (USD)']
    )
    trace1 = go.Scatter(
        x=df_uploaded_csv['Date'],
        y=df_uploaded_csv['BTC price in SK']
    )
    data = [trace0, trace1]
    layout=go.Layout(barmode='stack')
    fig.update_layout(title='US vs. non-US market',
                       xaxis_title='Month',
                       yaxis_title=f'{symbol}')
    fig=go.Figure(data=data, layout=layout)
    fig.show()
    py.iplot(data, filename = 'test')
    def to_pct(my_number):
        return f"{(my_number * 100):.4f}%"
    print("Today's date is: ")
    print(df_uploaded_csv['Date'][998])
    print("The daily market-close difference between markets is: ")
    percent_change = to_pct((df_uploaded_csv['BTC price in SK'][998]-df_uploaded_csv['close (USD)'][998])/df_uploaded_csv['close (USD)'][998])
    print(percent_change)
    to_float1 = percent_change.strip('%')
    to_float2 = float(to_float1)
    if to_float2 >= 5:
        print("Low-risk price arbitrage possible")
    else:
        print("Not worth the risk")
except Exception as err:
        print("OOPS, couldn't find that crypto. Please check your symbol and try again by re-running.")