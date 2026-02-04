<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>The Trade - Live Crypto Analysis</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        .chat-box { height: 300px; overflow-y: auto; border: 1px solid #333; }
        body { background-color: #0f172a; color: white; }
    </style>
</head>
<body class="p-5">

    <header class="text-center mb-10">
        <h1 class="text-4xl font-bold text-blue-400">THE TRADE</h1>
        <p class="text-gray-400">Created by: <span class="text-white font-semibold">Nitesh</span></p>
    </header>

    <div class="grid grid-cols-1 lg:grid-cols-2 gap-8">
        <div class="bg-slate-800 p-4 rounded-xl shadow-lg">
            <h2 class="text-xl mb-4">Bitcoin Live Analysis</h2>
            <div id="tradingview_chart" style="height: 400px;">
                <div class="tradingview-widget-container" style="height:100%;width:100%">
                    <iframe scrolling="no" allowtransparency="true" frameborder="0" src="https://s.tradingview.com/embed-widget/mini-symbol-overview/?locale=en#%7B%22symbol%22%3A%22BINANCE%3ABTCUSDT%22%2C%22width%22%3A%22100%25%22%2C%22height%22%3A%22100%25%22%2C%22dateRange%22%3A%221D%22%2C%22colorTheme%22%3A%22dark%22%2C%22trendLineColor%22%3A%22%2337a6ef%22%2C%22underLineColor%22%3A%22rgba(55%2C%20166%2C%20239%2C%200.15)%22%2C%22isTransparent%22%3Afalse%2C%22autosize%22%3Atrue%2C%22largeChartUrl%22%3A%22%22%7D" style="width: 100%; height: 100%;"></iframe>
                </div>
            </div>
        </div>

        <div class="bg-slate-800 p-4 rounded-xl shadow-lg">
            <h2 class="text-xl mb-4 text-green-400">Trade Assistant</h2>
            <div id="chatBox" class="chat-box bg-slate-900 p-3 rounded mb-4">
                <p class="text-gray-500">नमस्ते नितेश! मैं आपकी ट्रेडिंग में क्या मदद कर सकता हूँ?</p>
            </div>
            <div class="flex gap-2">
                <input type="text" id="userInput" placeholder="सवाल पूछें (उदा. तुम्हें किसने बनाया?)" class="flex-1 p-2 rounded bg-slate-700 border-none outline-none">
                <button onclick="askAssistant()" class="bg-blue-600 px-4 py-2 rounded hover:bg-blue-500">पूछें</button>
            </div>
        </div>
    </div>

    <script>
        function askAssistant() {
            const input = document.getElementById('userInput').value.toLowerCase();
            const chatBox = document.getElementById('chatBox');
            let response = "";

            if (input.includes("kisne banaya") || input.includes("creator")) {
                response = "मुझे *नितेश* ने बनाया है। वह एक विजनरी ट्रेडर और डेवलपर हैं।";
            } else if (input.includes("bitcoin") || input.includes("price")) {
                response = "अभी बिटकॉइन का चार्ट साइड में दिख रहा है। ट्रेंड बुलिश लग रहा है!";
            } else {
                response = "क्षमा करें, मैं अभी सीख रहा हूँ। आप नितेश से इसके बारे में पूछ सकते हैं।";
            }

            chatBox.innerHTML += <div class='mb-2'><b>आप:</b> ${document.getElementById('userInput').value}</div>;
            chatBox.innerHTML += <div class='mb-4 text-blue-300'><b>Assistant:</b> ${response}</div>;
            
            document.getElementById('userInput').value = "";
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    </script>

</body>
</html>
