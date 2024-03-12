import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.express as px

def fetch_stock_data(stock_symbol, start_date, end_date):
    # Fetch historical stock data
    stock_data = yf.download(stock_symbol, start=start_date, end=end_date)
    return stock_data

def main():
    st.title("Stock Closing Prices Visualization")

    # User input for stock symbol
    stock_symbol = st.text_input("Enter Stock Symbol (e.g., GOOG)")

    # User input for date range
    start_date = st.date_input("Select Start Date:", pd.to_datetime('2020-01-01'))
    end_date = st.date_input("Select End Date:", pd.to_datetime('2023-12-31'))

    # Fetch stock data
    stock_data = fetch_stock_data(stock_symbol, start_date, end_date)

    # Plot closing prices
    fig = px.line(stock_data['Close'], x=stock_data.index, y='Close', title=f"{stock_symbol} Closing Prices")
    fig.update_xaxes(title_text='Date')
    fig.update_yaxes(title_text='Closing Price (USD)')

    # Display the plot
    st.plotly_chart(fig)

if __name__ == "__main__":
    main()  