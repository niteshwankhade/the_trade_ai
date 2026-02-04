import streamlit as st
import streamlit.components.v1 as components

# पेज कॉन्फ़िगरेशन
st.set_page_config(layout="wide", page_title="The Trade AI Final")

# पूरा HTML कोड एक ही वेरिएबल में
terminal_code = """
<!DOCTYPE html>
<html>
<head>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body { background-color: #020617; color: #f8fafc; font-family: sans-serif; margin: 0; padding: 0; overflow: hidden; }
        .terminal-box { background: #0f172a; border: 2px solid #1e40af; border-radius: 12px; height: 90vh; }
        .chat-screen { height: 450px; overflow-y: auto; padding-right: 5px; }
        .chat-screen::-webkit-scrollbar { width: 4px; }
        .chat-screen::-webkit-scrollbar-thumb { background: #1e40af; border-radius: 10px; }
    </style>
</head>
<body class="p-4">
    <div class="flex flex-col lg:flex-row gap-4">
        <div class="flex-1 terminal-box p-4">
            <h1 class="text-blue-500 font-bold mb-2 italic">THE TRADE PRO v12.0</h1>
            <div class="w-full h-[550px] rounded-lg overflow-hidden border border-slate-800">
                <iframe id="mainChart" src="https://s.tradingview.com/widgetembed/?symbol=BINANCE:BTCUSDT&theme=dark&interval=60&style=1" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="w-full lg:w-96 terminal-box p-4 flex flex-col">
            <h2 class="text-emerald-400 font-bold border-b border-slate-800 pb-2 mb-4">SMC INTELLIGENCE</h2>
            <div id="chatBox" class="chat-screen space-y-4 mb-4 text-sm">
                <div class="bg-slate-800 p-3 rounded-lg border-l-4 border-blue-500">
                    <b>Assistant:</b> नमस्ते नितेश! सिस्टम अब स्थिर (Stable) है। <br> 'Gold' लिखें या पूछें 'किसने बनाया'।
                </div>
            </div>
            <div class="mt-auto flex gap-2">
                <input type="text" id="userInput" placeholder="यहाँ टाइप करें..." class="flex-1 bg-black border border-slate-700 p-3 rounded-xl text-white outline-none focus:border-blue-500">
                <button onclick="runCommand()" class="bg-blue-600 px-4 py-2 rounded-xl font-bold">RUN</button>
            </div>
        </div>
    </div>

    <script>
        const assets = { "gold": "OANDA:XAUUSD", "btc": "BINANCE:BTCUSDT", "nifty": "NSE:NIFTY" };

        function runCommand() {
            const val = document.getElementById('userInput').value.trim().toLowerCase();
            const chat = document.getElementById('chatBox');
            const chart = document.getElementById('mainChart');

            if(!val) return;

            chat.innerHTML += <div class='text-right'><span class='bg-blue-900/40 p-2 rounded-lg text-xs inline-block'>आप: ${val}</span></div>;

            let reply = "सिस्टम इसे स्कैन कर रहा है...";

            if(val.includes("kisne banaya") || val.includes("किसने बनाया")) {
                reply = "मुझे मास्टर माइंड <b>नितेश</b> ने बनाया है। मैं उनके ऑपरेटर माइंडसेट पर काम करता हूँ।";
            } else if(val.includes("indicator") || val.includes("diy")) {
                reply = "<b>🔥 टॉप इंडिकेटर्स:</b> DMI, VWAP और Fibonacci Golden Zone।";
            } else {
                let found = false;
                for (let key in assets) {
                    if (val.includes(key)) {
                        chart.src = https://s.tradingview.com/widgetembed/?symbol=${assets[key]}&theme=dark&interval=60;
                        reply = ${key.toUpperCase()} का चार्ट अपडेट कर दिया गया है।;
                        found = true; break;
                    }
                }
            }

            setTimeout(() => {
                chat.innerHTML += <div class='bg-slate-800 p-3 rounded-lg border-l-4 border-emerald-500'><b>The Trade:</b><br>${reply}</div>;
                chat.scrollTop = chat.scrollHeight;
            }, 200);
            document.getElementById('userInput').value = "";
        }

        // Enter key support
        document.getElementById("userInput").addEventListener("keyup", function(event) {
            if (event.keyCode === 13) { event.preventDefault(); runCommand(); }
        });
    </script>
</body>
</html>
"""

# यहाँ components.html को कॉल करना
components.html(terminal_code, height=800, scrolling=False)
