import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go

# पेज की सेटिंग
st.set_page_config(page_title="God-Level AI Trader", layout="wide")

# --- LOGIN SECTION ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    st.sidebar.title("🔐 Access Control")
    if st.sidebar.button("Login with Google 🆔"):
        st.session_state.logged_in = True
        st.rerun()
    st.title("🔒 कृपया लॉगिन करें")
    st.info("इस शक्तिशाली AI को एक्सेस करने के लिए साइडबार से लॉगिन करें।")
    st.stop()

# --- MAIN APP ---
st.title("🚀 God-Level Trading AI")
st.sidebar.success("Logged in as: User")

# --- परिचय और आपका नाम (CREATOR CREDITS) ---
st.sidebar.markdown("---")
st.sidebar.subheader("👤 Creator Details")
st.sidebar.write("Developed by: *Nitesh*")

# --- AI CHAT LOGIC ---
query = st.chat_input("मुझसे कुछ भी पूछें (जैसे: तुम्हें किसने बनाया है?)...")

if query:
    with st.chat_message("user"):
        st.write(query)
    
    with st.chat_message("assistant"):
        # अगर कोई आपके बारे में पूछे
        if "बनाया" in query or "creator" in query.lower() or "who made you" in query.lower() or "kaun hai" in query.lower():
            response = "मुझे *नीतीश (Nitesh)* ने बनाया है। मैं उनका निजी 'God-Level' ट्रेडिंग असिस्टेंट हूँ।"
        else:
            response = "मैं आपके डेटा का विश्लेषण कर रहा हूँ। चार्ट देखें और सही फैसला लें।"
        
        st.write(response)
        # आवाज़ वाला फीचर
        st.audio(f"https://translate.google.com/translate_tts?ie=UTF-8&q={response}&tl=hi&client=tw-ob", format="audio/mp3")

# --- TRADING SECTION ---
symbol = st.sidebar.text_input("शेयर का कोड (जैसे: TATAMOTORS.NS)", "RELIANCE.NS")

try:
    data = yf.download(symbol, period="1mo", interval="1d")
    if not data.empty:
        # Candlestick Chart
        fig = go.Figure(data=[go.Candlestick(
            x=data.index,
            open=data['Open'], high=data['High'],
            low=data['Low'], close=data['Close'],
            name="Market Data"
        )])
        fig.update_layout(title=f"{symbol} का लाइव कैंडलस्टिक चार्ट", template="plotly_dark")
        st.plotly_chart(fig, use_container_width=True)
        
        # Live Stats
        last_price = data['Close'].iloc[-1]
        st.metric(label=f"Current Price ({symbol})", value=f"₹{float(last_price):.2f}")
    else:
        st.warning("डेटा लोड नहीं हो सका। कृपया सही Ticker डालें।")
except Exception as e:
    st.error("एक तकनीकी समस्या आई है। कृपया कोड चेक करें।")



