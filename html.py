import yfinance as yf
import pandas as pd
import streamlit as st  # अगर आप Streamlit यूज़ कर रहे हैं तो, वरना इसे हटा सकते हैं

# 1. डेटा फेच करने का फंक्शन
def get_trading_data(symbol="RELIANCE.NS"):
    try:
        df = yf.download(symbol, period="5d", interval="15m")
        return df
    except Exception as e:
        return f"Error: {e}"

# 2. मेन फंक्शन जहाँ पूरा लॉजिक है
def start_app():
    print("--- Trading AI Started ---")
    st.title("My Trading AI Dashboard") # डैशबोर्ड का नाम
    
    symbol = "RELIANCE.NS"
    data = get_trading_data(symbol)
    
    if isinstance(data, pd.DataFrame) and not data.empty:
        st.write(f"Showing data for: {symbol}")
        st.line_chart(data['Close']) # क्लोजिंग प्राइस का चार्ट दिखाएगा
        st.dataframe(data.tail(10))  # आखिरी 10 कैंडल का डेटा
    else:
        st.error("डेटा लोड नहीं हो पाया।")

# 3. सबसे ज़रूरी हिस्सा (यही गलत था आपके फोटो में)
if _name_ == "_main_":
    # ऊपर वाले फंक्शन को कॉल करना
    try:
        # अगर आप streamlit run कर रहे हैं तो सीधा start_app() काम करेगा
        start_app()
    except Exception as e:
        # अगर कंसोल में चला रहे हैं
        print("App is running...")
        print(get_trading_data())
