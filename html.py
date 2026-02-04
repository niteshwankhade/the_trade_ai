<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NITESH AI - Operator Terminal</title>
    <script src="https://s3.tradingview.com/tv.js"></script>
    <style>
        :root { --primary: #00ff88; --bg: #050a10; --panel: #111b27; }
        body { margin: 0; font-family: 'Consolas', monospace; background: var(--bg); color: white; display: flex; height: 100vh; overflow: hidden; }
        
        /* Sidebar for AI */
        #ai-terminal { width: 400px; background: var(--panel); display: flex; flex-direction: column; border-right: 1px solid #2d4156; box-shadow: 5px 0 15px rgba(0,0,0,0.5); }
        .header { padding: 20px; background: #1a2635; border-bottom: 2px solid var(--primary); text-align: center; }
        .header h2 { margin: 0; color: var(--primary); font-size: 1.2rem; text-transform: uppercase; letter-spacing: 2px; }
        
        /* Chat Area */
        #chat-flow { flex: 1; overflow-y: auto; padding: 20px; display: flex; flex-direction: column; gap: 15px; scroll-behavior: smooth; }
        .msg { padding: 12px; border-radius: 8px; max-width: 85%; line-height: 1.4; font-size: 0.95rem; }
        .ai-msg { background: rgba(0, 255, 136, 0.1); border-left: 3px solid var(--primary); align-self: flex-start; }
        .user-msg { background: #2d4156; align-self: flex-end; color: #00ff88; }
        
        /* Input Area */
        .input-area { padding: 20px; background: #1a2635; display: flex; gap: 10px; }
        input { flex: 1; background: #050a10; border: 1px solid #2d4156; padding: 12px; color: white; border-radius: 5px; outline: none; }
        input:focus { border-color: var(--primary); }
        button { background: var(--primary); color: black; border: none; padding: 0 20px; border-radius: 5px; cursor: pointer; font-weight: bold; }

        /* Chart Area */
        #chart-canvas { flex: 1; position: relative; }
        .status-bar { position: absolute; top: 10px; right: 20px; background: rgba(0,0,0,0.7); padding: 5px 15px; border-radius: 20px; font-size: 12px; border: 1px solid var(--primary); z-index: 10; }
    </style>
</head>
<body>

<div id="ai-terminal">
    <div class="header">
        <h2>NITESH AI v1.0</h2>
        <small style="color: #64748b;">Operator Mindset Active</small>
    </div>
    <div id="chat-flow">
        <div class="msg ai-msg">प्रणाम। मैं नितेश द्वारा निर्मित एक एडवांस ट्रेडिंग ऑपरेटर AI हूँ। मार्केट का शिकार करने के लिए तैयार?</div>
    </div>
    <div class="input-area">
        <input type="text" id="userInput" placeholder="ऑपरेटर की तरह सोचें..." onkeypress="if(event.key==='Enter') processQuery()">
        <button onclick="processQuery()">SEND</button>
    </div>
</div>

<div id="chart-canvas">
    <div class="status-bar">● LIVE DATA FEED ACTIVE</div>
    <div id="tv_chart_container" style="height: 100%;"></div>
</div>

<script>
    // TradingView Chart Initialization
    new TradingView.widget({
        "autosize": true,
        "symbol": "BINANCE:BTCUSDT",
        "interval": "15",
        "timezone": "Asia/Kolkata",
        "theme": "dark",
        "style": "1",
        "locale": "in",
        "container_id": "tv_chart_container",
        "hide_side_toolbar": false,
        "allow_symbol_change": true,
        "details": true,
        "hotlist": true,
        "calendar": true
    });

    const chatFlow = document.getElementById('chat-flow');
    const synth = window.speechSynthesis;

    function speak(text) {
        const utter = new SpeechSynthesisUtterance(text);
        utter.lang = 'hi-IN';
        utter.rate = 1.1;
        utter.pitch = 1;
        synth.speak(utter);
    }

    function addMessage(text, type) {
        const div = document.createElement('div');
        div.className = msg ${type}-msg;
        div.innerText = text;
        chatFlow.appendChild(div);
        chatFlow.scrollTop = chatFlow.scrollHeight;
    }

    function processQuery() {
        const input = document.getElementById('userInput');
        const query = input.value.trim().toLowerCase();
        if (!query) return;

        addMessage(input.value, 'user');
        input.value = '';

        let response = "";

        // Intelligent Routing
        if (query.includes("बनाया") || query.includes("creator") || query.includes("owner")) {
            response = "मुझे 'नितेश' ने बनाया है। मैं उनके गॉड लेवल माइंडसेट और ऑपरेटर थ्योरी पर काम करता हूँ।";
        } 
        else if (query.includes("btc") || query.includes("bitcoin")) {
            response = "बिटकॉइन में अभी ऑपरेटर लिक्विडिटी हंट कर रहे हैं। 15 मिनट के चार्ट पर फेक-आउट से बचें। नितेश का नियम याद रखें: रिटेलर जहाँ फंसता है, हम वहीं एंट्री लेते हैं।";
        }
        else if (query.includes("ट्रेड") || query.includes("signal")) {
            response = "मार्केट अभी कंसोलिडेशन में है। हाई वॉल्यूम ब्रेकआउट का इंतज़ार करें। 90% सटीकता के लिए कन्फर्मेशन जरूरी है।";
        }
        else {
            response = "एनालिसिस पूरा हुआ। डेटा संकेत दे रहा है कि मार्केट बड़े मूव की तैयारी में है। नितेश के सिस्टम के अनुसार धैर्य ही पैसा है।";
        }

        // Delay for realism
        setTimeout(() => {
            addMessage(response, 'ai');
            speak(response);
        }, 600);
    }
</script>

</body>
</html>
