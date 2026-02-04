import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import urllib.parse

# 1. प्रोफेशनल 'The Trade' सेटअप
st.set_page_config(page_title="The Trade AI", layout="wide")

# 2. लॉगिन (Simple & Fast)
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False
if not st.session_state.logged_in:
    if st.sidebar.button("Login with Google 🆔"):
        st.session_state.logged_in = True
        st.rerun()
    st.title("🔒 The Trade - लॉगिन करें")
    st.stop()

# 3. साइडबार - केवल ज़रूरी जानकारी
st.sidebar.title("📈 The Trade")
st.sidebar.write("Creator: *Nitesh*")
asset = st.sidebar.selectbox('Asset चुनें:', ('Bitcoin', 'Gold', 'USD/INR', 'Nifty 50'))
symbols = {'Bitcoin':'BTC-USD', 'Gold':'GC=F', 'USD/INR':'INR=X', 'Nifty 50':'^NSEI'}
sym = symbols[asset]

# 4. लाइव चार्ट इंजन (काली स्क्रीन का अंत)
st.title(f"🚀 {asset} लाइव एनालिसिस")
try:
    # 5 दिन का डेटा ताकि ग्राफ हमेशा साफ़ दिखे
    df = yf.download(sym, period="5d", interval="15m")
    
    if not df.empty:
        # असली कैंडलस्टिक चार्ट
        fig = go.Figure(data=[go.Candlestick(
            x=df.index, open=df['Open'], high=df['High'],
            low=df['Low'], close=df['Close'],
            increasing_line_color='#00ff00', decreasing_line_color='#ff0000'
        )])
        fig.update_layout(template="plotly_dark", xaxis_rangeslider_visible=False, height=450)
        st.plotly_chart(fig, use_container_width=True)
        
        # भाव को साफ़ नंबर में बदलना (Junk टेक्स्ट हटाने के लिए)
        last_price = round(float(df['Close'].iloc[-1]), 2)
    else:
        st.error("डेटा नहीं मिला।")
        last_price = 0
except Exception:
    st.error("मार्केट से कनेक्शन टूट गया है।")
    last_price = 0

# 5. स्मार्ट टॉकिंग AI (मेरे जैसा सटीक जवाब)
st.markdown("---")
st.subheader("🤖 The Trade असिस्टेंट")
user_input = st.text_input("मुझसे पूछें (जैसे: भाव क्या है? या तुम कौन हो?):", key="main_chat")

if user_input:
    user_q = user_input.lower()
    
    # सटीक जवाब का लॉजिक
    if any(word in user_q for word in ["बनाया", "creator", "kaun hai", "nitesh"]):
        final_ans = "मुझे नीतीश ने बनाया है। मैं 'The Trade' का स्मार्ट एआई हूँ।"
    elif any(word in user_q for word in ["bhav", "price", "market", "rate"]):
        final_ans = f"नीतीश, अभी {asset} का भाव {last_price} चल रहा है।"
    else:
        final_ans = f"नीतीश, {asset} का ताज़ा भाव {last_price} है। क्या आप ट्रेड करना चाहते हैं?"

    # स्क्रीन पर साफ़ जवाब
    st.chat_message("assistant").write(final_ans)

    # वॉइस फिक्स (0:00 एरर खत्म)
    clean_text = urllib.parse.quote(final_ans)
    audio_url = f"https://translate.google.com/translate_tts?ie=UTF-8&q={clean_text}&tl=hi&client=tw-ob"
    
    st.write("📢 *सुनने के लिए प्ले दबाएं:*")
    st.audio(audio_url, format="audio/mp3")

