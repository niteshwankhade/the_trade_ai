import streamlit as st
import streamlit.components.v1 as components

# पेज की सेटिंग्स
st.set_page_config(layout="wide", page_title="The Trade")

# HTML और CSS कोड को एक वेरिएबल में डालना
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .chat-box { height: 350px; overflow-y: auto; background: #1e293b; border-radius: 8px; padding: 15px; }
        body { background-color: #0f172a; color: white; font-family: sans-serif; }
        .user-msg { color: #60a5fa; margin-bottom: 10px; }
        .ai-msg { color: #34d399; margin-bottom: 20px; border-bottom: 1px solid #334155; padding-bottom: 10px; }
    </style>
</head>
<body>
    <div style="text-align: center; margin-bottom: 20px;">
        <h1 style="color: #60a5fa; font-size: 30px; font-weight: bold;">THE TRADE</h1>
        <p style="color: #94a3b8;">Created by: Nitesh</p>
    </div>

    <div style="display: flex; gap: 20px; flex-wrap: wrap;">
        <div style="flex: 1; min-width: 300px; background: #1e293b; padding: 15px; border-radius: 12px;">
            <h3 style="margin-bottom: 15px;">Bitcoin Live Analysis</h3>
            <iframe scrolling="no" allowtransparency="true" frameborder="0" src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?locale=en#%7B%22symbol%22%3A%22BINANCE%3ABTCUSDT%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A250%2C%22dateRange%22%3A%221D%22%2C%22colorTheme%22%3A%22dark%22%2C%22trendLineColor%22%3A%22%2337a6ef%22%2C%22underLineColor%22%3A%22rgba(55%2C%20166%2C%20239%2C%200.15)%22%2C%22isTransparent%22%3Afalse%2C%22autosize%22%3Atrue%7D" style="width: 100%; height: 250px;"></iframe>
        </div>

        <div style="flex: 1; min-width: 300px; background: #1e293b; padding: 15px; border-radius: 12px;">
            <h3 style="margin-bottom: 15px; color: #34d399;">Trade Assistant</h3>
            <div id="chatBox" class="chat-box">
                <div class="ai-msg"><b>Assistant:</b> नमस्ते नितेश! मैं तैयार हूँ। पूछिए क्या पूछना है?</div>
            </div>
            <div style="margin-top: 15px; display: flex; gap: 10px;">
                <input type="text" id="userInput" style="flex: 1; padding: 10px; border-radius: 5px; border: none; background: #334155; color: white;" placeholder="यहाँ टाइप करें...">
                <button onclick="ask()" style="background: #2563eb; color: white; padding: 10px 20px; border: none; border-radius: 5px; cursor: pointer;">पूछें</button>
            </div>
        </div>
    </div>

    <script>
        function ask() {
            let input = document.getElementById('userInput').value;
            let chat = document.getElementById('chatBox');
            if(!input) return;

            chat.innerHTML += <div class="user-msg"><b>आप:</b> ${input}</div>;
            
            let reply = "मैं अभी डेटा प्रोसेस कर रहा हूँ।";
            if(input.toLowerCase().includes("kisne banaya")) {
                reply = "मुझे *नितेश* ने बनाया है, जो एक एक्सपर्ट ट्रेडर हैं।";
            } else if(input.toLowerCase().includes("bitcoin")) {
                reply = "बिटकॉइन का लाइव चार्ट आपके सामने है, मार्केट अभी दिलचस्प लग रहा है!";
            }

            chat.innerHTML += <div class="ai-msg"><b>Assistant:</b> ${reply}</div>;
            document.getElementById('userInput').value = "";
            chat.scrollTop = chat.scrollHeight;
        }
    </script>
</body>
</html>
"""

# Streamlit को बताना कि यह HTML है
components.html(html_code, height=600, scrolling=True)
