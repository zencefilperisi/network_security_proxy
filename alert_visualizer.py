import matplotlib.pyplot as plt
import datetime
from collections import Counter
import re

# alert.log dosyasını oku
with open("logs/alert.log", "r", encoding="utf-8") as f:
    lines = f.readlines()

# Tür ve saat bilgilerini ayır
alert_types = []
alert_hours = []

for line in lines:
    # Tür belirleme
    if "Suspicious URL" in line:
        alert_types.append("URL")
    elif "Suspicious POST" in line:
        alert_types.append("POST")
    elif "Large POST" in line:
        alert_types.append("Large POST")
    elif "Brute-force" in line:
        alert_types.append("Brute-force")
    else:
        alert_types.append("Other")

    # Saat bilgisi çıkar
    match = re.search(r"at (\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})", line)
if match:
    timestamp = datetime.datetime.strptime(match.group(1), "%Y-%m-%d %H:%M:%S")
    hour = timestamp.strftime("%Y-%m-%d %H:00")
    alert_hours.append(hour)

# Alarm türü sayımı
type_counts = Counter(alert_types)

# Saatlik alarm yoğunluğu
hour_counts = Counter(alert_hours)

# 📊 Grafik 1: Alarm Türü Dağılımı
plt.figure(figsize=(6, 4))
plt.bar(type_counts.keys(), type_counts.values(), color="crimson")
plt.title("Alarm Türü Dağılımı")
plt.xlabel("Alarm Türü")
plt.ylabel("Sayı")
plt.tight_layout()
plt.grid(axis='y')
plt.show()

# 📈 Grafik 2: Saat Bazlı Alarm Sayısı
plt.figure(figsize=(10, 4))
hours_sorted = sorted(hour_counts.items())
hours, counts = zip(*hours_sorted)
plt.plot(hours, counts, marker="o", color="darkblue")
plt.title("Saatlik Alarm Yoğunluğu")
plt.xlabel("Zaman (Saat)")
plt.ylabel("Alarm Sayısı")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()
