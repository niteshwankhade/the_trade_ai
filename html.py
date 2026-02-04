mport streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import urllib.parse

st.set_page_config(page_title="Nitesh God-Level AI", layout="wide")

# --- LOGIN ---
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    if st.sidebar.button("Login with Google 🆔"):
        st.session_state.logged_in = True
        st.rerun()
    st.stop()

# --- SIDEBAR ---
st.sidebar.title("👤 Creator: Nitesh")
option = st.sidebar.selectbox('Asset चुनें:', ('Bitcoin (BTC-USD)', 'Gold (GC=F)', 'USD/INR', 'NIFTY 50 (^NSEI)'))
symbol_dict = {'Bitcoin (BTC-USD)':'BTC-USD', 'Gold (GC=F)':'GC=F', 'USD/INR':'INR=X', 'NIFTY 50 (^NSEI)':'^NSEI'}
symbol = symbol_dict[option]

# --- DATA FETCHING (विदेशी बाजार के लिए सुधार) ---
data = pd.DataFrame() # शुरुआत में खाली बॉक्स
try:
    # 2 दिन का डेटा ताकि चार्ट खाली न रहे
    data = yf.download(symbol, period="2d", interval="15m")
except Exception as e:
    st.error("इंटरनेट या डेटा सर्वर में समस्या है।")

# --- CHART ---
if not data.empty and len(data) > 1:
    st.subheader(f"📊 {option} लाइव चार्ट")
    fig = go.Figure(data=[go.Candlestick(
        x=data.index, open=data['Open'], high=data['High'],
        low=data['Low'], close=data['Close']
    )])
    fig.update_layout(xaxis_rangeslider_visible=False, template="plotly_dark", height=450)
    st.plotly_chart(fig, use_container_width=True)
    current_p = data['Close'].iloc[-1]
else:
    st.warning("⚠️ अभी मार्केट डेटा उपलब्ध नहीं है, लेकिन AI चालू है।")
    current_p = "उपलब्ध नहीं"

# --- AI VOICE CHAT (TypeError Fix) ---
st.markdown("---")
st.subheader("🤖 नीतीश का बोलने वाला AI")
user_input = st.text_input("मुझसे बात करें:", placeholder="जैसे: तुम्हें किसने बनाया है?")

if user_input:
    if any(x in user_input.lower() for x in ["बनाया", "creator", "kaun hai"]):
        reply = "मुझे नीतीश ने बनाया है। मैं एक गॉड लेवल ट्रेडिंग एआई हूँ।"
    else:
        reply = f"नीतीश, {option} का भाव अभी {current_p} है। मैं मार्केट देख रहा हूँ।"

    st.write(f"🗨️ *AI:* {reply}")
    
    # ऑडियो लिंक
    encoded_msg = urllib.parse.quote(reply)
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={encoded_msg}&tl=hi&client=tw-ob"
    st.audio(audio_url, format="audio/mp3")
   

