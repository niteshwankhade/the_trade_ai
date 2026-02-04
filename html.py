import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import urllib.parse

# 1. पेज की मजबूत सेटिंग
st.set_page_config(page_title="Nitesh God-Level AI", layout="wide")

# 2. सुरक्षित लॉगिन (Google Style)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.sidebar.title("🔐 Access")
    if st.sidebar.button("Login with Google 🆔"):
        st.session_state.logged_in = True
        st.rerun()
    st.title("🔒 कृपया लॉगिन करें")
    st.info("नीतीश के खास AI का उपयोग करने के लिए लॉगिन बटन दबाएं।")
    st.stop()

# 3. साइडबार - यहाँ से आप गोल्ड या बिटकॉइन बदल सकते हैं
st.sidebar.title("👤 Creator: Nitesh")
st.sidebar.markdown("---")
option = st.sidebar.selectbox('क्या देखना चाहते हैं?', 
    ('Bitcoin (BTC-USD)', 'Gold (GC=F)', 'USD/INR', 'NIFTY 50 (^NSEI)', 'Reliance (RELIANCE.NS)'))

symbol_dict = {
    'Bitcoin (BTC-USD)':'BTC-USD', 'Gold (GC=F)':'GC=F', 
    'USD/INR':'INR=X', 'NIFTY 50 (^NSEI)':'^NSEI', 'Reliance (RELIANCE.NS)':'RELIANCE.NS'
}
symbol = symbol_dict[option]

# 4. कैंडलस्टिक चार्ट (लाइन वाली समस्या का परमानेंट इलाज)
# interval='5m' से कैंडल मोटी और साफ़ दिखती हैं
try:
    data = yf.download(symbol, period="1d", interval="5m")
    
    if not data.empty:
        st.subheader(f"📊 {option} लाइव कैंडलस्टिक चार्ट")
        
        # असली कैंडलस्टिक डेटा
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'], high=data['High'],
            low=data['Low'], close=data['Close'],
            increasing_line_color='#26A69A', decreasing_line_color='#EF5350' # असली ट्रेडिंग कलर्स
        )])

        fig.update_layout(
            xaxis_rangeslider_visible=False, 
            template="plotly_dark", 
            height=500,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # लाइव प्राइस मीटर
        current_price = data['Close'].iloc[-1]
        st.metric(label="लाइव मार्केट भाव", value=f"{current_price:.2f}")

    else:
        st.error("बाज़ार का डेटा अभी नहीं मिल रहा। कृपया इंटरनेट चेक करें।")
except Exception as e:
    st.error("डेटा लोड करने में समस्या आई।")

# 5. AI आवाज़ (पढ़कर सुनाने वाली समस्या का परमानेंट इलाज)
st.markdown("---")
st.subheader("🤖 नीतीश का बोलने वाला AI")

user_query = st.text_input("मुझसे सवाल पूछें (जैसे: तुम्हें किसने बनाया?):")

if user_query:
    # जवाब का लॉजिक
    if any(word in user_query.lower() for word in ["बनाया", "creator", "who made you", "kaun hai", "नीतीश"]):
        reply = "मुझे नीतीश ने बनाया है। मैं उनका गॉड लेवल ट्रेडिंग एआई हूँ और उनके इशारे पर काम करता हूँ।"
    else:
        reply = f"नीतीश, {option} का भाव अभी {current_price:.2f} है। मेरे हिसाब से आपको सावधानी से ट्रेड करना चाहिए।"

    # टेक्स्ट और ऑडियो एक साथ
    st.ch
