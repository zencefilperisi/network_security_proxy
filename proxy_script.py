from mitmproxy import http
import datetime
import os
from collections import defaultdict
from colorama import Fore, Style, init
from telegram_notifier import send_telegram_message

init()

# Log klasörü yoksa oluştur
if not os.path.exists("logs"):
    os.makedirs("logs")

# IP bazlı istek zamanlarını takip için
request_times = defaultdict(list)

# Şüpheli URL ve içerik anahtar kelimeleri
suspicious_keywords = ["admin", "login", "passwd", "shell", "cmd"]
post_keywords = ["password", "credit", "card", "token", "api_key"]

# Uyarı fonksiyonu (sadece kırmızı yazı + log)
def alert(message):
    print(Fore.RED + message + Style.RESET_ALL)
    with open("logs/alert.log", "a", encoding="utf-8") as f:
        f.write(message + "\n")
    send_telegram_message(message)

# Trafiği analiz eden ana fonksiyon
def request(flow: http.HTTPFlow):
    now = datetime.datetime.now()
    now_str = now.strftime("%Y-%m-%d %H:%M:%S")
    url = flow.request.pretty_url
    method = flow.request.method
    content = flow.request.get_text()
    client_ip = flow.client_conn.peername[0]

    # Temel trafik loglama
    log_entry = f"[{now_str}] {client_ip} - {method} {url}"
    print(log_entry)
    with open("logs/http_traffic.log", "a", encoding="utf-8") as f:
        f.write(log_entry + "\n")

    # Şüpheli URL kontrolü
    if any(word in url.lower() for word in suspicious_keywords):
        alert(f"[ALERT] Suspicious URL at {now_str}: {url} from {client_ip}")

    # Şüpheli POST içerik kontrolü
    if method == "POST":
        if any(k in content.lower() for k in post_keywords):
            alert(f"[ALERT] Suspicious POST Content at {now_str}: {url} from {client_ip}")

        if len(content) > 1000:
            alert(f"[ALERT] Large POST Data at {now_str}: {url} ({len(content)} bytes) from {client_ip}")

    # Brute-force saldırı kontrolü (10 saniyede 10'dan fazla istek)
    request_times[client_ip].append(now)
    window_start = now - datetime.timedelta(seconds=10)
    recent = [t for t in request_times[client_ip] if t > window_start]
    request_times[client_ip] = recent

    if len(recent) > 10:
        alert(f"[ALERT] Possible Brute-force from {client_ip} at {now_str} ({len(recent)} requests in 10s)")
