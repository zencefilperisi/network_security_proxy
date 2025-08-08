import matplotlib.pyplot as plt
from collections import Counter
import datetime
import re

# Log dosyasını oku
with open("logs/http_traffic.log", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Zaman, IP ve URL bilgilerini ayıkla
timestamps = []
ips = []
urls = []

for line in lines:
    match = re.match(r"\[(.*?)\] (.*?) - (\w+) (.*)", line)
    if match:
        time_str, ip, method, url = match.groups()
        time = datetime.datetime.strptime(time_str, "%Y-%m-%d %H:%M:%S")
        timestamps.append(time)
        ips.append(ip)
        urls.append(url)

# Saatlik trafik hacmi
hours = [t.replace(minute=0, second=0) for t in timestamps]
hour_counter = Counter(hours)

# En çok istek yapan IP'ler
ip_counter = Counter(ips).most_common(5)

# En sık ziyaret edilen URL'ler
url_counter = Counter(urls).most_common(5)

# 📈 Grafik 1: Saatlik trafik
plt.figure(figsize=(10, 5))
plt.plot(list(hour_counter.keys()), list(hour_counter.values()), marker='o')
plt.title("Saatlik Trafik Hacmi")
plt.xlabel("Zaman")
plt.ylabel("İstek Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()

# 📊 Grafik 2: En Çok İstek Gönderen IP’ler
labels, values = zip(*ip_counter)
plt.figure(figsize=(6, 4))
plt.bar(labels, values, color="orange")
plt.title("En Çok İstek Gönderen IP’ler")
plt.xlabel("IP Adresi")
plt.ylabel("İstek Sayısı")
plt.tight_layout()
plt.show()

# 📊 Grafik 3: En Sık Ziyaret Edilen URL’ler
labels, values = zip(*url_counter)
plt.figure(figsize=(6, 4))
plt.barh(labels, values, color="purple")
plt.title("En Sık Ziyaret Edilen URL’ler")
plt.xlabel("İstek Sayısı")
plt.tight_layout()
plt.show()
