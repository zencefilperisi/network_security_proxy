# **Network Security Proxy**
A **Python-based HTTP/HTTPS proxy** that monitors network traffic in real time, detects suspicious requests, and sends instant alerts via **Telegram**.  
Includes **visualization tools** for analyzing alerts and traffic logs.

## 🚀 Features
- 🔍 Detects suspicious URLs, POST content, large POST data, and brute-force attempts  
- 📩 Sends instant alerts to a Telegram chat  
- 📝 Logs all HTTP/HTTPS traffic  
- 📊 Visualization scripts for alerts (`alert_visualizer.py`) and logs (`log_visualizer.py`)  
- ⚡ Easy to set up and run  

## 📦 Installation
```bash
git clone https://github.com/<username>/network_security_proxy.git
cd network_security_proxy
pip install -r requirements.txt

⚙️ Usage
1. Add your Telegram bot token and chat ID in telegram_notifier.py.
2. Start the proxy:
mitmdump -s proxy_script.py
3. Configure your browser’s proxy settings:
Host: localhost
Port: 8080
4. Browse the web to generate traffic and test detection.

📊 Visualization
- Generate alert and log graphs:
python alert_visualizer.py
python log_visualizer.py

📌 Requirements
- Python 3.8+
- mitmproxy
- colorama
- matplotlib
- python-telegram-bot

⚠️ Disclaimer
This tool is for educational and testing purposes only.
Do not use it on networks you do not own or have permission to monitor.

💡 Developed with ❤️ for network monitoring enthusiasts.
