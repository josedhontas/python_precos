import yfinance as yf

def get_financial_data():
    try:
        brent = yf.Ticker("BZ=F")
        historico_brent = brent.history(period="1d")
        brent_price = historico_brent["Close"].iloc[-1] if not historico_brent.empty else None

        dolar = yf.Ticker("USDBRL=X")
        historico_dolar = dolar.history(period="1d")
        dollar_price = historico_dolar["Close"].iloc[-1] if not historico_dolar.empty else None

        return {
            "brent_price": brent_price,
            "dollar_price": dollar_price
        }
    except Exception as e:
        raise RuntimeError(f"Error fetching financial data: {e}")
