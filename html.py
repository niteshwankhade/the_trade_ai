import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(layout="wide", page_title="The Trade AI | Nitesh Edition", initial_sidebar_state="collapsed")

# CSS and HTML Logic for the Ultimate Terminal
html_code = """
<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@400;700&family=Inter:wght@300;500;700&display=swap" rel="stylesheet">
    <style>
        body { background: #05070a; color: #e2e8f0; font-family: 'Inter', sans-serif; overflow: hidden; }
        .terminal-header { font-family: 'Orbitron', sans-serif; letter-spacing: 2px; text-shadow: 0 0 10px #3b82f6; }
        .glass-card { background: rgba(15, 23, 42, 0.8); backdrop-filter: blur(12px); border: 1px solid rgba(59, 130, 246, 0.2); border-radius: 16px; }
        .chat-container { height: 480px; overflow-y: auto; scrollbar-width: thin; scrollbar-color: #3b82f6 #0f172a; }
        .glow-button { background: linear-gradient(90deg, #1e40af, #3b82f6); transition: all 0.3s ease; box-shadow: 0 0 15px rgba(59, 130, 246, 0.4); }
        .glow-button:hover { transform: scale(1.05); box-shadow: 0 0 25px rgba(59, 130, 246, 0.6); }
        .operator-msg { border-left: 4px solid #10b981; background: rgba(16, 185, 129, 0.05); }
    </style>
</head>
<body class="p-2">

    <div class="flex justify-between items-center mb-4 px-4 bg-slate-900/50 py-2 rounded-xl border border-slate-800">
        <div>
            <h1 class="terminal-header text-2xl font-bold text-blue-500">THE TRADE <span class="text-white text-xs opacity-50">v4.0 PRO</span></h1>
            <p class="text-[10px] text-slate-400">ARCHITECT: NITESH | SMC & OPERATOR ALGO ENABLED</p>
        </div>
        <div class="flex gap-4">
            <div class="text-right">
                <p class="text-[10px] text-slate-500">SYSTEM STATUS</p>
                <p class="text-xs text-green-400 font-bold">● ACTIVE ANALYSER</p>
            </div>
        </div>
    </div>

    <div class="grid grid-cols-12 gap-4">
        
        <div class="col-span-12 lg:col-span-8 glass-card p-2 relative">
            <div class="absolute top-4 left-4 z-10 bg-black/60 px-3 py-1 rounded text-xs font-bold border border-blue-500/30">
                <span id="currentAsset">BTC/USDT</span> | 1H | CANDLES
            </div>
            <div id="chart_box" class="w-full h-[600px] rounded-xl overflow-hidden">
                <iframe id="tv_chart" src="https://s.tradingview.com/widgetembed/?frameElementId=tradingview_1&symbol=BINANCE:BTCUSDT&interval=60&hidesidetoolbar=0&symboledit=1&saveimage=1&toolbarbg=111827&studies=[]&theme=dark&style=1&timezone=Asia%2FKolkata" class="w-full h-full" frameborder="0"></iframe>
            </div>
        </div>

        <div class="col-span-12 lg:col-span-4 flex flex-col gap-4">
            <div class="glass-card p-4 flex-1 flex flex-col">
                <h3 class="text-blue-400 font-bold mb-3 flex items-center gap-2">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path d="M13 10V3L4 14h7v7l9-11h-7z"/></svg>
                    OPERATOR INTELLIGENCE
                </h3>
                
                <div id="chatBox" class="chat-container space-y-4 mb-4 p-2 text-sm">
                    <div class="operator-msg p-3 rounded-r-lg">
                        <b>The Trade:</b> नमस्ते नितेश। मार्केट स्ट्रक्चर बुलिश है पर 'Inducement' का इंतज़ार करें। आप किस एसेट का शिकार करना चाहते हैं?
                    </div>
                </div>

                <div class="relative mt-auto">
                    <input type="text" id="userInput" placeholder="Ask SMC Target (e.g. Gold Chart)..." class="w-full bg-slate-900 border border-slate-700 rounded-xl p-4 pr-16 text-sm outline-none focus:border-blue-500 transition-all">
                    <butt
