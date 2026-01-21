if st.button("Compare Stocks"):

    if ticker1 == "" or ticker2 == "":
        st.error("Please enter both ticker symbols.")

    else:
        try:
            data1 = yf.download(
                ticker1,
                interval="1mo",
                progress=False
            )

            data2 = yf.download(
                ticker2,
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
            ax.legend()
            st.pyplot(fig)

        except Exception as e:
            st.error("Error fetching data.")
            st.write(str(e))
