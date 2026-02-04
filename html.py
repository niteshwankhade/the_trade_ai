import yfinance as yf
import pandas as pd
import time

# 1. स्टॉक की सेटिंग्स
SYMBOL = "RELIANCE.NS"  # आप यहाँ अपना स्टॉक बदल सकते हैं
SHORT_WINDOW = 20        # छोटा मूविंग एवरेज
LONG_WINDOW = 50         # बड़ा मूविंग एवरेज

def fetch_and_analyze():
    print(f"--- Fetching Data for {SYMBOL} ---")
    
    # डेटा डाउनलोड करना (पिछले 5 दिन का, 15 मिनट के अंतराल पर)
    data = yf.download(SYMBOL, period="5d", interval="15m", progress=False)
    
    if data.empty:
        print("Error: डेटा नहीं मिल रहा। कृपया इंटरनेट या सिंबल चेक करें।")
        return

    # 2. इंडिकेटर्स कैलकुलेट करना (SMA)
    data['SMA20'] = data['Close'].rolling(window=SHORT_WINDOW).mean()
    data['SMA50'] = data['Close'].rolling(window=LONG_WINDOW).mean()

    # 3. Buy/Sell लॉजिक
    last_row = data.iloc[-1]
    prev_row = data.iloc[-2]

    print(f"Current Price: {last_row['Close']:.2f}")
    print(f"SMA20: {last_row['SMA20']:.2f} | SMA50: {last_row['SMA50']:.2f}")

    if prev_row['SMA20'] < prev_row['SMA50'] and last_row['SMA20'] > last_row['SMA50']:
        print("📢 SIGNAL: BUY (Golden Cross detected!)")
    elif prev_row['SMA20'] > prev_row['SMA50'] and last_row['SMA20'] < last_row['SMA50']:
        print("📢 SIGNAL: SELL (Death Cross detected!)")
    else:
        print("📢 SIGNAL: HOLD (No crossover yet)")

# रन करने के लिए
if _name_ == "_main_":
    try:
        fetch_and_analyze()
    except Exception as e:
        print(f"An error occurred: {e}")
