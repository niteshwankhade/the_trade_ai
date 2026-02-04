import streamlit as st
import streamlit.components.v1 as components

# पेज की सेटिंग
st.set_page_config(layout="wide", page_title="The Trade Pro AI")

# सबसे मजबूत और वर्किंग HTML कोड
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #020617; color: #f8fafc; font-family: sans-serif; overflow: hidden; }
        .glass-panel { background: #0f172a; border: 1px solid #1e40af; border-radius: 15px; }
        .chat-box { height: 480px; overflow-y: auto; scrollbar-width: none; }
        .btn-blue { background: #2563eb; transition: 0.2s; }
        .btn-blue:hover { background: #3b82f6; transform: scale(1.02); }
    </style>
</head>
<body class="p-4">
    <div class="flex flex-col lg:flex-row gap-4">
        
        <div class="flex-1 glass-panel p-4">
            <div class="flex justify-between items-center mb-3">
                <h1 class="text-xl font-bold text-blue-500">THE TRADE AI v10.0</h1>
                <span id="assetTitle" class="text-xs text-slate-400 font-mono">ASSET: BITCOIN</span>
            </div>
            <div id="chartDiv" class="w-full h-[550px] rounded-xl overflow-hidden border border-slate-800">
                <iframe id="tradingViewFrame" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&hidesidetoolbar=0&saveimage=1&style=1&timezone=Asia%2FKolkata" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-96 glass-panel p-4 flex flex-col">
            <h2 class="text-emerald-400 font-bold mb-4 border-b border-slate-800 pb-2 flex items-center gap-2">
                <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
                AI STRATEGY HUB
            </h2>
            
            <div id="displayArea" class="chat-box space-y-4 mb-4 pr-1">
                <div class="bg-slate-800/50 p-3 rounded-lg border-l-4 border-blue-500 text-sm">
                    <b>System:</b> नमस्ते नितेश! मैं तैयार हूँ। <br><br>
                    गोल्ड देखने के लिए <b>'Gold'</b> लिखें और इंडिकेटर के लिए <b>'DIY'</b>।
                </div>
            </div>

            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="Ask Gold, BTC or Indicator..." class="flex-1 bg-black border border-slate-700 rounded-xl p-3 text-sm outline-none focus:border-blue-500 text-white">
                <button onclick="handleAction()" class="btn-blue text-white px-4 py-2 rounded-xl font-bold text-xs uppercase">Run</button>
            </div>
        </div>
    </div>

    <script>
        const symbols = {
            "gold": "OANDA:XAUUSD",
            "bitcoin": "BINANCE:BTCUSDT",
            "btc": "BINANCE:BTCUSDT",
            "nifty": "NSE:NIFTY",
            "eth": "BINANCE:ETHUSDT"
        };

        function handleAction() {
            const input = document.getElementById('userInput').value.toLowerCase();
            const chat = document.getElementById('displayArea');
            const chart = document.getElementById('tradingViewFrame');
            const title = document.getElementById('assetTitle');

            if (!input) return;

            // User Message
            chat.innerHTML += <div class="text-right"><span class="bg-blue-600/20 text-blue-300 p-2 rounded-lg text-xs inline-block italic">Query: ${input}</span></div>;

            let response = "डेटा स्कैन किया जा रहा है...";
            let found = false;

            // Indicator Logic
            if (input.includes("diy") || input.includes("indicator") || input.includes("इंडिकेटर")) {
                response = "<b>✅ इंडिकेटर एनालिसिस:</b><br><br>1. <b>DMI (DIY):</b> ट्रेंड की ताकत (ADX) 25 से ऊपर होनी चाहिए।<br>2. <b>VWAP:</b> बड़े प्लेयर्स की एंट्री लेवल चेक करें।<br>3. <b>Fibonacci:</b> 0.618 लेवल पर नज़र रखें।";
                found = true;
            }

            // Asset Switch Logic
            for (let key in symbols) {
                if (input.includes(key)) {
                    chart.src = https://s.tradingview.com/widgetembed/?symbol=${symbols[key]}&theme=dark&interval=60&hidesidetoolbar=0&symboledit=1&style=1;
                    title.innerText = "ASSET: " + key.toUpperCase();
                    response = <b>${key.toUpperCase()} चार्ट लोड हो गया है!</b><br>मार्केट स्ट्रक्चर अभी 'High Liquidity' ज़ोन में है।;
                    found = true;
                    break;
                }
            }

            if (!found && input.includes("kisne banaya")) {
                response = "मुझे मास्टर माइंड <b>नितेश</b> ने बनाया है।";
            }

            setTimeout(() => {
                chat.innerHTML += <div class="bg-slate-800/80 p-3 rounded-lg border-l-4 border-emerald-500 text-sm"><b>The Trade:</b><br>${response}</div>;
                chat.scrollTop = chat.scrollHeight;
            }, 300);

            document.getElementById('userInput').value = "";
        }
    </script>
</body>
</html>
"""

# Streamlit Component Call
components.html(html_code, height=720, scrolling=False)
