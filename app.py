import streamlit as st
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

st.title("Stock Comparison App")
st.write("Compare two stocks using normalized adjusted close prices (last 5 years).")

ticker1 = st.text_input("Enter first ticker symbol (e.g. AAPL)")
ticker2 = st.text_input("Enter second ticker symbol (e.g. MSFT)")

if st.button("Compare Stocks"):

    if ticker1 == "" or ticker2 == "":
        st.error("Please enter both ticker symbols.")

    else:
        try:
            end_date = datetime.today()
            start_date = end_date - timedelta(days=5*365)

            data1 = yf.download(
                ticker1,
                start=start_date,
                end=end_date,
                interval="1mo",
                progress=False
            )

            data2 = yf.download(
                ticker2,
                start=start_date,
                end=end_date,
                interval="1mo",
                progress=False
            )

            if data1.empty:
                st.error(f"Invalid ticker: {ticker1}")
                st.stop()

            if data2.empty:
                st.error(f"Invalid ticker: {ticker2}")
                st.stop()

            adj1 = data1["Adj Close"]
            adj2 = data2["Adj Close"]

            norm1 = adj1 / adj1.iloc[0]
            norm2 = adj2 / adj2.iloc[0]

            fig, ax = plt.subplots()
            ax.plot(norm1.index, norm1, label=ticker1.upper())
            ax.plot(norm2.index, norm2, label=ticker2.upper())

            ax.set_title("Normalized Adjusted Close Comparison")
            ax.set_xlabel("Date")
            ax.set_ylabel("Normalized Price")
            ax.legend()
            ax.grid(True)

            st.pyplot(fig)

        except Exception as e:
            st.error("Error fetching data.")
            st.write(str(e))
