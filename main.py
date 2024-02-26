import yfinance as yf

def ask_for_symbol():
    global symbol
    symbol = input("Input stock symbol: ")

def get_stock_price():
    # Download stock data with additional information (adjust params as needed)
    data = yf.download(symbol, period="5d", interval="1d", auto_adjust=True)

    # Access values using iloc for clarity
    current_price = data.iloc[-1]["Close"]  # Last closing price
    previous_close = data.iloc[-2]["Close"]  # Price from the previous day

    # Try to access market cap, handle potential absence gracefully
    try:
        market_cap = data.iloc[-1]["Market Cap"]
        print(f"Market capitalization: {market_cap}")
    except KeyError:
        print("Market capitalization data not available.")

    # Print the information
    print(f"Current price of {symbol}: {current_price}")
    print(f"Change from previous day: {current_price - previous_close:.2f}")

while (True):
   ask_for_symbol() 
   get_stock_price()