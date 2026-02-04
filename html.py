import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import urllib.parse

# पेज कॉन्फ़िगरेशन
st.set_page_config(page_title="The Trade", layout="wide")

# --- LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    if st.sidebar.button("Login with Google 🆔"):
        st.session_state.logged_in = True
        st.rerun()
    st.title("🔒 The Trade - लॉगिन करें")
    st.stop()

# --- SIDEBAR ---
st.sidebar.title("📈 The Trade")
st.sidebar.write("Developed by: *Nitesh*")
asset = st.sidebar.selectbox('Asset चुनें:', ('Bitcoin', 'Gold', 'USD/INR', 'Nifty 50'))
symbols = {'Bitcoin':'BTC-USD', 'Gold':'GC=F', 'USD/INR':'INR=X', 'Nifty 50':'^NSEI'}
sym = symbols[asset]

# --- LIVE CHART ENGINE ---
st.title("📊 The Trade - Live Analysis")
try:
    # 5 दिन का डेटा ताकि चार्ट खाली न रहे
    df = yf.download(sym, period="5d", interval="15m")
    
    if not df.empty:
        fig = go.Figure(data=[go.Candlestick(
            x=df.index, open=df['Open'], high=df['High'],
            low=df['Low'], close=df['Close'],
            increasing_line_color='#00ff00', decreasing_line_color='#ff0000'
        )])
        fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=500)
        st.plotly_chart(fig, use_container_width=True)
        
        # साफ़ भाव (Clean Price for AI)
        last_price = float(df['Close'].iloc[-1])
    else:
        st.error("डेटा नहीं मिला।")
        last_price = 0
except Exception:
    st.error("मार्केट डेटा लोड नहीं हो सका।")
    last_price = 0

# --- THE TRADE AI (बोलने वाला) ---
st.markdown("---")
st.subheader("🤖 The Trade AI Assistant")
query = st.text_input("मुझसे पूछें (जैसे: मार्केट कैसा है? या तुम्हें किसने बनाया?):")

if query:
    query_l = query.lower()
    # 1. क्रिएटर का सवाल
    if any(word in query_l for word in ["बनाया", "creator", "kaun hai", "nitesh"]):
        ans = "मुझे नीतीश ने बनाया है। मैं 'The Trade' का एक्सपर्ट एआई हूँ।"
    
    # 2. मार्केट का हाल
    elif any(word in query_l for word in ["market", "bhav", "price", "halat", "kaisa"]):
        trend = "ऊपर जा रहा है" if df['Close'].iloc[-1] > df['Open'].iloc[-1] else "नीचे गिर रहा है"
        ans = f"नीतीश, {asset} का भाव अभी {last_price:.2f} है और मार्केट अभी {trend}।"
    
    # 3. जनरल ट्रेडिंग ज्ञान
    else:
        ans = f"ट्रेडिंग में डिसिप्लिन ज़रूरी है। {asset} का ताज़ा भाव {last_price:.2f} है, सोच-समझकर ट्रेड करें।"

    # साफ़ जवाब दिखाएं
    st.chat_message("assistant").write(ans)

    # साफ़ आवाज़ (No junk text)
    clean_msg = urllib.parse.quote(ans)
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={clean_msg}&tl=hi&client=tw-ob"
    st.audio(audio_url, format="audio/mp3")



