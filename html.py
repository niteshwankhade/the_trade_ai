import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="The Trade AI - Final Fix")

# क्लीन और वर्किंग कोड
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #020617; color: #f8fafc; font-family: ui-sans-serif, system-ui; overflow: hidden; }
        .terminal { background: #0f172a; border: 2px solid #1e40af; border-radius: 16px; }
        .chat-screen { height: 500px; overflow-y: auto; scroll-behavior: smooth; }
        .chat-screen::-webkit-scrollbar { width: 0px; }
        .input-field { background: #020617; border: 1px solid #334155; border-radius: 12px; color: white; }
        .input-field:focus { border-color: #3b82f6; outline: none; }
    </style>
</head>
<body class="p-4">
    <div class="flex flex-col lg:flex-row gap-6">
        
        <div class="flex-1 terminal p-4">
            <div class="flex justify-between items-center mb-4">
                <h1 class="text-xl font-black text-blue-500 italic">THE TRADE PRO v11.0</h1>
                <div id="status" class="text-[10px] bg-blue-900/30 text-blue-400 px-2 py-1 rounded">SYSTEM: ONLINE</div>
            </div>
            <div class="w-full h-[580px] rounded-xl overflow-hidden border border-slate-800">
                <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&style=1" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-[400px] terminal p-4 flex flex-col">
            <h2 class="text-emerald-400 font-bold mb-4 border-b border-slate-800 pb-2 flex items-center gap-2">
                <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
                OPERATOR INTELLIGENCE
            </h2>
            
            <div id="chatBox" class="chat-screen space-y-4 mb-4 text-sm p-1">
                <div class="bg-slate-800/50 p-3 rounded-lg border-l-4 border-blue-500">
                    <b>The Trade:</b> नमस्ते नितेश! मैं तैयार हूँ। <br><br>
                    एसेट का नाम (Gold, BTC) या सवाल टाइप करें।
                </div>
            </div>

            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="यहाँ लिखें..." class="input-field flex-1 p-3 text-sm">
                <button onclick="process()" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-xl font-bold transition-all">RUN</button>
            </div>
        </div>
    </div>

    <script>
        // Enter Key Support
        document.getElementById("userInput").addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                process();
            }
        });

        const assets = {
            "gold": "OANDA:XAUUSD",
            "bitcoin": "BINANCE:BTCUSDT",
            "btc": "BINANCE:BTCUSDT",
            "nifty": "NSE:NIFTY",
            "eth": "BINANCE:ETHUSDT"
        };

        function process() {
            const inputField = document.getElementById('userInput');
            const input = inputField.value.trim().toLowerCase();
            const chat = document.getElementById('chatBox');
            const chart = document.getElementById('mainChart');

            if (!input) return;

            // User Chat Bubble
            chat.innerHTML += <div class="flex justify-end"><div class="bg-blue-600/20 text-blue-300 p-2 rounded-lg text-xs italic border border-blue-500/20">आप: ${input}</div></div>;

            let reply = "क्षमा करें, मैं समझ नहीं पाया। कृपया 'Gold' या 'Indicator' लिखकर देखें।";

            // 1. Creator Question (Priority)
            if (input.includes("kisne banaya") || input.includes("किसने बनाया")) {
                import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="The Trade AI - Final Fix")

# क्लीन और वर्किंग कोड
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #020617; color: #f8fafc; font-family: ui-sans-serif, system-ui; overflow: hidden; }
        .terminal { background: #0f172a; border: 2px solid #1e40af; border-radius: 16px; }
        .chat-screen { height: 500px; overflow-y: auto; scroll-behavior: smooth; }
        .chat-screen::-webkit-scrollbar { width: 0px; }
        .input-field { background: #020617; border: 1px solid #334155; border-radius: 12px; color: white; }
        .input-field:focus { border-color: #3b82f6; outline: none; }
    </style>
</head>
<body class="p-4">
    <div class="flex flex-col lg:flex-row gap-6">
        
        <div class="flex-1 terminal p-4">
            <div class="flex justify-between items-center mb-4">
                <h1 class="text-xl font-black text-blue-500 italic">THE TRADE PRO v11.0</h1>
                <div id="status" class="text-[10px] bg-blue-900/30 text-blue-400 px-2 py-1 rounded">SYSTEM: ONLINE</div>
            </div>
            <div class="w-full h-[580px] rounded-xl overflow-hidden border border-slate-800">
                <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&style=1" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-[400px] terminal p-4 flex flex-col">
            <h2 class="text-emerald-400 font-bold mb-4 border-b border-slate-800 pb-2 flex items-center gap-2">
                <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
                OPERATOR INTELLIGENCE
            </h2>
            
            <div id="chatBox" class="chat-screen space-y-4 mb-4 text-sm p-1">
                <div class="bg-slate-800/50 p-3 rounded-lg border-l-4 border-blue-500">
                    <b>The Trade:</b> नमस्ते नितेश! मैं तैयार हूँ। <br><br>
                    एसेट का नाम (Gold, BTC) या सवाल टाइप करें।
                </div>
            </div>

            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="यहाँ लिखें..." class="input-field flex-1 p-3 text-sm">
                <button onclick="process()" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-xl font-bold transition-all">RUN</button>
            </div>
        </div>
    </div>

    <script>
        // Enter Key Support
        document.getElementById("userInput").addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                process();
            }
        });

        const assets = {
            "gold": "OANDA:XAUUSD",
            "bitcoin": "BINANCE:BTCUSDT",
            "btc": "BINANCE:BTCUSDT",
            "nifty": "NSE:NIFTY",
            "eth": "BINANCE:ETHUSDT"
        };

        function process() {
            const inputField = document.getElementById('userInput');
            const input = inputField.value.trim().toLowerCase();
            const chat = document.getElementById('chatBox');
            const chart = document.getElementById('mainChart');

            if (!input) return;

            // User Chat Bubble
            chat.innerHTML += <div class="flex justify-end"><div class="bg-blue-600/20 text-blue-300 p-2 rounded-lg text-xs italic border border-blue-500/20">आप: ${input}</div></div>;

            let reply = "क्षमा करें, मैं समझ नहीं पाया। कृपया 'Gold' या 'Indicator' लिखकर देखें।";

            // 1. Creator Question (Priority)
            if (input.includes("kisne banaya") || input.includes("किसने बनाया")) {
                import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="The Trade AI - Final Fix")

# क्लीन और वर्किंग कोड
html_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background: #020617; color: #f8fafc; font-family: ui-sans-serif, system-ui; overflow: hidden; }
        .terminal { background: #0f172a; border: 2px solid #1e40af; border-radius: 16px; }
        .chat-screen { height: 500px; overflow-y: auto; scroll-behavior: smooth; }
        .chat-screen::-webkit-scrollbar { width: 0px; }
        .input-field { background: #020617; border: 1px solid #334155; border-radius: 12px; color: white; }
        .input-field:focus { border-color: #3b82f6; outline: none; }
    </style>
</head>
<body class="p-4">
    <div class="flex flex-col lg:flex-row gap-6">
        
        <div class="flex-1 terminal p-4">
            <div class="flex justify-between items-center mb-4">
                <h1 class="text-xl font-black text-blue-500 italic">THE TRADE PRO v11.0</h1>
                <div id="status" class="text-[10px] bg-blue-900/30 text-blue-400 px-2 py-1 rounded">SYSTEM: ONLINE</div>
            </div>
            <div class="w-full h-[580px] rounded-xl overflow-hidden border border-slate-800">
                <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&style=1" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-[400px] terminal p-4 flex flex-col">
            <h2 class="text-emerald-400 font-bold mb-4 border-b border-slate-800 pb-2 flex items-center gap-2">
                <span class="w-2 h-2 bg-emerald-500 rounded-full animate-pulse"></span>
                OPERATOR INTELLIGENCE
            </h2>
            
            <div id="chatBox" class="chat-screen space-y-4 mb-4 text-sm p-1">
                <div class="bg-slate-800/50 p-3 rounded-lg border-l-4 border-blue-500">
                    <b>The Trade:</b> नमस्ते नितेश! मैं तैयार हूँ। <br><br>
                    एसेट का नाम (Gold, BTC) या सवाल टाइप करें।
                </div>
            </div>

            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="यहाँ लिखें..." class="input-field flex-1 p-3 text-sm">
                <button onclick="process()" class="bg-blue-600 hover:bg-blue-500 text-white px-6 py-2 rounded-xl font-bold transition-all">RUN</button>
            </div>
        </div>
    </div>

    <script>
        // Enter Key Support
        document.getElementById("userInput").addEventListener("keypress", function(event) {
            if (event.key === "Enter") {
                process();
            }
        });

        const assets = {
            "gold": "OANDA:XAUUSD",
            "bitcoin": "BINANCE:BTCUSDT",
            "btc": "BINANCE:BTCUSDT",
            "nifty": "NSE:NIFTY",
            "eth": "BINANCE:ETHUSDT"
        };

        function process() {
            const inputField = document.getElementById('userInput');
            const input = inputField.value.trim().toLowerCase();
            const chat = document.getElementById('chatBox');
            const chart = document.getElementById('mainChart');

            if (!input) return;

            // User Chat Bubble
            chat.innerHTML += <div class="flex justify-end"><div class="bg-blue-600/20 text-blue-300 p-2 rounded-lg text-xs italic border border-blue-500/20">आप: ${input}</div></div>;

            let reply = "क्षमा करें, मैं समझ नहीं पाया। कृपया 'Gold' या 'Indicator' लिखकर देखें।";

            // 1. Creator Question (Priority)
            if (input.includes("kisne banaya") || input.includes("किसने बनाया")) {
                reply = "मुझे मास्टर माइंड <b>नितेश</b> ने बनाया है। मैं उनके 'Operator Mindset' और 'SMC' लॉजिक पर काम करने वाला दुनिया का सबसे पावरफुल AI हूँ।";
            } 
            // 2. Indicator Question
            else if (input.includes("indicator") || input.includes("diy") || input.includes("इंडिकेटर")) {
                reply = "<b>🔥 प्रो इंडिकेटर लिस्ट:</b><br><br>1. <b>DMI/ADX:</b> ट्रेंड की ताकत नापने के लिए।<br>2. <b>MACD:</b> मोमेंटम कन्फर्मेशन के लिए।<br>3. <b>VWAP:</b> बड़े पैसे की एंट्री देखने के लिए।";
            }
            // 3. Asset Switching
            else {
                let found = false;
                for (let key in assets) {
                    if (input.includes(key)) {
                        chart.src = https://s.tradingview.com/widgetembed/?symbol=${assets[key]}&theme=dark&interval=60&style=1;
                        reply = <b>${key.toUpperCase()} विश्लेषण:</b> चार्ट अपडेट कर दिया गया है। 'Price Action' अब बुलिश/बेरिश मोड में स्कैन हो रहा है।;
                        found = true;
                        break;
                    }
                }
                if (!found) {
                    reply = "मैं इस एसेट को अभी ट्रैक नहीं कर पा रहा हूँ। कृपया Gold या BTC आज़माएँ।";
                }
            }

            // Assistant Reply Bubble
            setTimeout(() => {
                chat.innerHTML += <div class="bg-slate-800 p-3 rounded-lg border-l-4 border-emerald-500 shadow-lg text-white"><b>The Trade:</b><br>${reply}</div>;
                chat.scrollTop = chat.scrollHeight;
            }, 200);

            inputField.value = "";
        }
    </script>
</body>
</html>
"""



