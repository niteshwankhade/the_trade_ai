import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="The Trade AI | DMI Edition")

html_code = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #010409; color: #e6edf3; font-family: 'Inter', sans-serif; overflow: hidden; }
        .terminal-bg { background: #0d1117; border: 1px solid #30363d; border-radius: 12px; }
        .chat-area { height: 500px; overflow-y: auto; scrollbar-width: none; }
        .logic-bubble { background: #161b22; border-left: 4px solid #1f6feb; border-radius: 4px; }
        .user-bubble { background: #0d1117; border: 1px solid #30363d; text-align: right; color: #58a6ff; }
    </style>
</head>
<body class="p-4">

    <div class="flex flex-col lg:flex-row gap-4">
        <div class="flex-1 terminal-bg p-4 shadow-xl">
            <div class="flex justify-between items-center mb-3">
                <h1 class="text-xl font-bold text-blue-500">THE TRADE AI <span class="text-xs text-gray-500 italic">v9.0 DMI PRO</span></h1>
                <div class="text-[10px] text-green-500 font-mono">ENCRYPTED CONNECTION: ACTIVE</div>
            </div>
            <div class="w-full h-[580px] rounded-lg overflow-hidden border border-[#30363d]">
                <iframe id="mainFrame" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&hidesidetoolbar=0&saveimage=1&style=1&timezone=Asia%2FKolkata" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-96 terminal-bg p-4 flex flex-col">
            <div class="border-b border-[#30363d] pb-2 mb-4">
                <h2 class="text-blue-400 font-semibold flex items-center gap-2">
                    <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 20 20"><path d="M11 3a1 1 0 10-2 0v1a1 1 0 102 0V3zM15.657 5.757a1 1 0 00-1.414-1.414l-.707.707a1 1 0 001.414 1.414l.707-.707zM18 10a1 1 0 01-1 1h-1a1 1 0 110-2h1a1 1 0 011 1zM5.05 6.464A1 1 0 106.464 5.05l-.707-.707a1 1 0 00-1.414 1.414l.707.707zM5 10a1 1 0 01-1 1H3a1 1 0 110-2h1a1 1 0 011 1zM8 16v-1a1 1 0 112 0v1a1 1 0 11-2 0zM13.333 16a1 1 0 110-2c.667 0 1.333-.333 1.333-1s-.667-1-1.333-1a1 1 0 110-2c1.333 0 2.667.667 2.667 2s-1.333 2-2.667 2z"></path></svg>
                    DMI/ADX LOGIC ENGINE
                </h2>
            </div>
            
            <div id="chatDisplay" class="chat-area space-y-3 pr-2 mb-4">
                <div class="logic-bubble p-3 text-sm">
                    <b>System:</b> नमस्ते नितेश। <b>DMI (D.I.Y)</b> इंडिकेटर अब आपके कमांड्स के लिए तैयार है। <br><br>
                    एनालिसिस के लिए <b>"DIY"</b> या <b>"Indicator"</b> लिखें।
                </div>
            </div>

            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="Ask DMI Strategy..." class="flex-1 bg-black border border-[#30363d] rounded-lg p-3 text-sm focus:outline-none focus:border-blue-500">
                <button onclick="processInput()" class="bg-[#238636] hover:bg-[#2ea043] text-white font-bold px-4 py-2 rounded-lg text-xs">EXECUTE</button>
            </div>
        </div>
    </div>

    <script>
        const symbols = { "gold": "OANDA:XAUUSD", "btc": "BINANCE:BTCUSDT", "nifty": "NSE:NIFTY", "eth": "BINANCE:ETHUSDT" };

        function processInput() {
            const input = document.getElementById('userInput').value.toLowerCase();
            const chat = document.getElementById('chatDisplay');
            const frame = document.getElementById('mainFrame');

            if(!input) return;

            chat.innerHTML += <div class="user-bubble p-2 rounded-lg text-xs italic mb-2">Query: ${input}</div>;

            let res = "एनालिसिस लोड हो रहा है...";

            if(input.includes("diy") || input.includes("dmi") || input.includes("indicator")) {
                res = `<b>📊 DMI (D.I.Y) एक्सपर्ट रिपोर्ट:</b><br><br>
                       📍 <b>+DI > -DI:</b> मार्केट में खरीदार (Bulls) हावी हैं।<br>
                       📍 <b>-DI > +DI:</b> मार्केट में विक्रेता (Sellers) हावी हैं।<br>
                       📉 <b>ADX (Trend Strength):</b> अगर ADX 25 के ऊपर है, तो मौजूदा ट्रेंड बहुत मजबूत है।<br><br>
                       💡 <b>Nitesh's Strategy:</b> जब +DI, -DI को क्रॉस करे और ADX ऊपर जा रहा हो, तो वह जैकपॉट ट्रेड होता है।`;
            } else if(input.includes("kisne banaya")) {
                res = "मुझे मास्टर माइंड <b>नितेश</b> ने बनाया है। मैं उनके ट्रेडिंग विजन का हिस्सा हूँ।";
            }

            for(let key in symbols) {
                if(input.includes(key)) {
                    frame.src = https://s.tradingview.com/widgetembed/?symbol=${symbols[key]}&theme=dark&interval=60;
                    res = <b>${key.toUpperCase()} एनालिसिस:</b> चार्ट अपडेटेड। DMI लेवल पर नज़र रखें!;
                }
            }

            setTimeout(() => {
                chat.innerHTML += <div class="logic-bubble p-3 text-sm text-blue-100 mb-4"><b>The Trade AI:</b><br>${res}</div>;
                chat.scrollTop = chat.scrollHeight;
            }, 300);

            document.getElementById('userInput').value = "";
        }
    </script>
</body>
</html>
"""

components.html(html_code, height=720, scrolling=False) 
